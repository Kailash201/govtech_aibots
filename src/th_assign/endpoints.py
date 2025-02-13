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


@app.get("/agents")
async def create_agent():
    tmp = await AgentModel(name="tmp").insert()
    return tmp
    pass


@app.get("/agents/{agent_id}")
def get_agent():

    #return id, name
    pass


@app.delete("/agents/{agent_id}")
def delete_agent():
    pass


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
