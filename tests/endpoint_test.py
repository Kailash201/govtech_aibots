from fastapi.testclient import TestClient
from th_assign.main import app


client = TestClient(app)
global agent_id

def test_create_agent():
    global agent_id
    with TestClient(app) as client:
        files = [
            ('files', open('tests/files/file-sample_100kB.pdf', 'rb')),
            ('files', open('tests/files/file-sample_100kB.docx', 'rb')),
            ('files', open('tests/files/file_example_XLSX_10.xlsx', 'rb')),
            ('files', open('tests/files/tests-example.xls', 'rb')),
            ('files', open('tests/files/SamplePPTFile_500kb.ppt', 'rb')),
            ('files', open('tests/files/samplepptx.pptx', 'rb')),
            ]

        websites = {
            "websites": [
                "https://www.cancer.gov/about-cancer/understanding/what-is-cancer",
                "https://www.mayoclinic.org/diseases-conditions/cancer/expert-answers/heart-cancer/faq-20058130"
            ]
        }
        

        response = client.post("/agents", files=files, data=websites)
        print(response.text)
        assert response.status_code == 201
        res = response.json()
        assert res.get("agent_id") != None
        agent_id = res.get("agent_id")

def test_get_agent():
    global agent_id
    with TestClient(app) as client:
        response = client.get(f"/agents/{agent_id}")
        assert response.status_code == 200
        res = response.json()
        assert res.get("_id") != None
        assert res.get("name") != None
        assert res.get("files") != None
        assert res.get("websites") != None
        
def test_extract_websites():
    global agent_id    
    with TestClient(app) as client:
        websites = {
            "urls": [
                "https://www.cancer.gov/about-cancer/understanding/what-is-cancer",
                "https://www.mayoclinic.org/diseases-conditions/cancer/expert-answers/heart-cancer/faq-20058130"
            ]
        }
        response = client.put(f"/agents/{agent_id}/websites", json=websites)
        print(response.text)
        assert response.status_code == 204
        

def test_extract_files():
    global agent_id
    files = [
        ('files', open('tests/files/file-sample_100kB.pdf', 'rb')),
        ('files', open('tests/files/file-sample_100kB.docx', 'rb')),
        ('files', open('tests/files/file_example_XLSX_10.xlsx', 'rb')),
        ('files', open('tests/files/tests-example.xls', 'rb')),
        ('files', open('tests/files/SamplePPTFile_500kb.ppt', 'rb')),
        ('files', open('tests/files/samplepptx.pptx', 'rb')),
        ]
    
    with TestClient(app) as client:
        response = client.put(f"/agents/{agent_id}/files", files=files)
        assert response.status_code == 204

def test_query_agent():
    global agent_id
    with TestClient(app) as client:
        query = {'query': "What is cancer?"}
        response = client.post(f"/agents/{agent_id}/queries", json=query)
        assert response.status_code == 201
        res = response.json()
        assert res.get("agent_response") != None
        assert isinstance(res.get("agent_response"), str)



def test_delete_agent():
    with TestClient(app) as client:
        response = client.delete(f"/agents/{agent_id}")
        assert response.status_code == 204