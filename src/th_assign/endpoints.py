from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "home"


@app.post("/agents")
def create_agent():
    
    #return id
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
