from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, HTTPException
import os
from typing import List
import uuid

from .agent import Agent
from .database import Database
from .models.beanieModels import AgentModel, FileDocument, WebsiteDocument
from .models.filetypes.modelFactory import FileModelFactory
from .models.reqModels import WebsiteReq, QueryReq
from .tools import wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.init()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/agents", status_code=201)
async def create_agent(files: List[UploadFile] | None, websites: List[str] | None):
    files_to_save: List[FileDocument] = [
        FileDocument(
            name=f.filename, 
            content=await f.read(), 
            content_type=os.path.splitext(f.filename)[-1],
            extracted_content=None)
        for f in files
        ]
    
    websites_to_save: List[WebsiteDocument] = [
        WebsiteDocument(
            url=url,
            extracted_content=None
        )
        for url in websites
    ]

    new_agent = await AgentModel(
        name="ResearchAgent",
        files=files_to_save,
        websites=websites_to_save,
        ).insert()

    to_ret = {
        "agent_id": new_agent.id
    }
    
    return to_ret


@app.get("/agents/{agent_id}")
async def get_agent(agent_id: str):
    agentDoc = await AgentModel.get(uuid.UUID(agent_id))
    to_ret = {
        "_id": agentDoc.id,
        "name": agentDoc.name,
        "files": [f.name for f in agentDoc.files],
        "websites": [w.url for w in agentDoc.websites],
        "messages": []
    }

    return to_ret


@app.delete("/agents/{agent_id}", status_code=204)
async def delete_agent(agent_id: str):
    agentDoc = await AgentModel.find_one(AgentModel.id == uuid.UUID(agent_id))
    await agentDoc.delete()
    return 

    
@app.put("/agents/{agent_id}/websites", status_code=204)
async def extract_websites(agent_id: str, websites: WebsiteReq):
    agentDoc = await AgentModel.find_one(AgentModel.id == uuid.UUID(agent_id))
    websites_to_extract = [
        (FileModelFactory.create(agent_ws_doc), agent_ws_doc)
        for url in websites.urls for agent_ws_doc in agentDoc.websites if url == agent_ws_doc.url
    ]
    
    for webModel, webDoc in websites_to_extract:
        extracted_text = webModel.extract_text()
        webDoc.extracted_content = extracted_text
    
    await agentDoc.save()
        
    return

    
@app.put("/agents/{agent_id}/files", status_code=204)
async def extract_files(agent_id: str, files: List[UploadFile]):
    agentDoc = await AgentModel.find_one(AgentModel.id == uuid.UUID(agent_id))
    files_to_extract = [
        (FileModelFactory.create(agent_file_doc), agent_file_doc)
        for f in files for agent_file_doc in agentDoc.files if f.filename == agent_file_doc.name
    ]
    
    for fileModel, fileDoc in files_to_extract:
        extracted_text = fileModel.extract_text()
        print(fileModel.get_extension())
        print(extracted_text)
        print()
        fileDoc.extracted_content = extracted_text
    await agentDoc.save()
    
    return


@app.post("/agents/{agent_id}/queries", status_code=201)
async def query_agent(agent_id: str, query: QueryReq):
    tools = [wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool]
    agentDoc = await AgentModel.find_one(AgentModel.id == uuid.UUID(agent_id))
    
    context_from_websites = ""
    for web in agentDoc.websites:
        if web.extracted_content:
            context_from_websites += web.extracted_content

    context_from_files = ""
    for cus_file in agentDoc.files:
        if cus_file.extracted_content:
            context_from_files += cus_file.extracted_content
    
    total_context = context_from_files + "\n" + context_from_websites

    agent = Agent(
        tools=tools,
        model_name='gpt-4o-mini'
    )

    context_tokens = agent.tokenize(total_context)
    
    if context_tokens > 120000:
        return HTTPException(
            status_code=413,
            detail= "The knowledge added to agent exceeds the maximum allowable context of 120k tokens",
            headers={"Error": "ExceededLLMContextLimit"}
            )
    
    res = agent.invoke_agent(
        knowledge_base=total_context, 
        query=query.query
        )
    
    to_ret = {
        "agent_response": res
    }
    return to_ret
