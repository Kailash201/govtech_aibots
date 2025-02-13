from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import Database, AgentModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.init()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "home"


@app.post("/agents")
async def create_agent():
    new_agent = await AgentModel(_id=4, name="ResearchAgent").insert()
    return new_agent.id


@app.get("/agents/{agent_id}")
async def get_agent(agent_id: int):
    agentDoc = await AgentModel.find_one(AgentModel.id == agent_id)
    #return id, name
    return agentDoc


@app.delete("/agents/{agent_id}")
async def delete_agent(agent_id: int):
    agentDoc = await AgentModel.find_one(AgentModel.id == agent_id)
    await agentDoc.delete()
    return True


@app.put("/agents/{agent_id}/websites")
def todo():
    pass

@app.put("/agents/{agent_id}/files")
def todo():
    pass


@app.put("/agents/{agent_id}/queries")
def query_agent():
    #return response
    pass
