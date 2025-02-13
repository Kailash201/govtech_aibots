from fastapi.testclient import TestClient
from th_assign.endpoints import app


client = TestClient(app)

# def test_create_agent():
#     with TestClient(app) as client:
#         response = client.post("/agents")
#         assert response.status_code == 201
#         assert response.json().get("agent_id") != None

def test_get_agent():
    with TestClient(app) as client:
        response = client.get("/agents/2")
        assert response.status_code == 200
        assert response.json().get("_id") != None
        assert response.json().get("name") != None


def test_delete_agent():
    with TestClient(app) as client:
        response = client.delete("/agents/6")
        assert response.status_code == 204


def test_query_agent():
    response = client.post("/agents/2/queries")
    assert response.status_code == 201
    assert response.json().get("agent_response") != None