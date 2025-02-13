from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import Database
from .models import AgentModel, Query
from .agent import Agent
from .tools import wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool

from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.init()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "home"


@app.post("/agents", status_code=201)
async def create_agent(files: List[str], websites: List[str]):
    new_agent = await AgentModel(
        name="ResearchAgent",
        files=files,
        websites=websites
        ).insert()
    
    to_ret = {
        "agent_id": new_agent.id
    }
    return to_ret


@app.get("/agents/{agent_id}")
async def get_agent(agent_id: int):
    agentDoc = await AgentModel.find_one(AgentModel.id == agent_id)
    return agentDoc


@app.delete("/agents/{agent_id}", status_code=204)
async def delete_agent(agent_id: int):
    agentDoc = await AgentModel.find_one(AgentModel.id == agent_id)
    await agentDoc.delete()
    return 


@app.put("/agents/{agent_id}/websites")
def todo():
    pass

@app.put("/agents/{agent_id}/files")
def todo():
    pass


@app.post("/agents/{agent_id}/queries", status_code=201)
def query_agent(agent_id: int, message: Query):
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
