from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from .database import Database
from .models import AgentModel, Query
from .agent import Agent

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.init()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "home"


@app.post("/agents", status_code=201)
async def create_agent():
    new_agent = await AgentModel(_id=6, name="ResearchAgent").insert()
    to_ret = {
        "agent_id": new_agent
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
    from .tools import wikipedia_tool, arxiv_tool, pubmed_tool, ddg_search_tool
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
