from fastapi import FastAPI, File, UploadFile
from contextlib import asynccontextmanager

from .database import Database
from .models import AgentModel, Query, FileDocument
from .agent import Agent
from .tools import wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool

from typing import List
import uuid

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.init()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "home"


@app.post("/agents", status_code=201)
async def create_agent(files: List[UploadFile] | None, websites: List[str] | None):
    files_to_save: List[FileDocument] = [
        FileDocument(
            name=f.filename, 
            content=await f.read(), 
            content_type=f.content_type,
            extracted_content=None)
        for f in files
        ]
    
    new_agent = await AgentModel(
        name="ResearchAgent",
        files=files_to_save,
        websites=websites,
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
        "websites": agentDoc.websites,
        "messages": []
    }

    ## TESTING, TO DELETE
    from .filetypes.pdfModel import PDFModel
    from .filetypes.docModel import DOCModel
    from .filetypes.docxModel import DOCXModel
    from .filetypes.pptModel import PPTModel
    from .filetypes.pptxModel import PPTXModel
    from .filetypes.xlsModel import XLSModel
    from .filetypes.xlsxModel import XLSXModel

    tmp = PPTModel(
        filename="sdf",
        content=agentDoc.files[0].content
    )
    print(tmp.extract_text())
    return to_ret


@app.delete("/agents/{agent_id}", status_code=204)
async def delete_agent(agent_id: str):
    agentDoc = await AgentModel.find_one(AgentModel.id == uuid.UUID(agent_id))
    await agentDoc.delete()
    return 


@app.put("/agents/{agent_id}/websites")
def todo():
    # from unstructured.partition.pdf import partition_pdf
    
    # print(files)
    
    
    # tmp = await files.read()
    # elements = partition_pdf(file=files.file)
    # for e in elements:
    #     print(e.text)
    # print(elements)
    pass

@app.put("/agents/{agent_id}/files")
def todo():
    pass


@app.post("/agents/{agent_id}/queries", status_code=201)
def query_agent(agent_id: str, message: Query):
    tools = [wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool]
    agent = Agent(
        tools=tools,
        model_name='gpt-4o-mini'
    )
    res = agent.invoke_agent(message)
    to_ret = {
        "agent_response": res
    }
    return to_ret
