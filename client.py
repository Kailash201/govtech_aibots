import httpx
import asyncio

async def create_agent_request():
    url = "http://localhost:8000/agents"  

    # ADD THE FILES HERE
    files = [
            ('files', open('tests/files/file-sample_100kB.pdf', 'rb')),
            ('files', open('tests/files/file-sample_100kB.docx', 'rb')),
            ('files', open('tests/files/file_example_XLSX_10.xlsx', 'rb')),
            ('files', open('tests/files/tests-example.xls', 'rb')),
            ('files', open('tests/files/SamplePPTFile_500kb.ppt', 'rb')),
            ('files', open('tests/files/samplepptx.pptx', 'rb')),
        ]
    
    # ADD THE WEBSITES HERE
    data = {
        "websites": [
            "https://www.mayoclinic.org/diseases-conditions/lung-cancer/symptoms-causes/syc-20374620",
            "https://www.gleneagles.com.sg/conditions-diseases/lung-cancer/symptoms-causes"
        ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, files=files, data=data, timeout=None)
        if response.status_code == 201:
            return response.json()  
        else:
            return {"error": "Failed to create agent", "status_code": response.status_code}

async def extract_files(agent_id):
    agent_id = agent_id
    rl = "http://localhost:8000/agents" 
    req = "files"

    files = [
            ('files', open('tests/files/file-sample_100kB.pdf', 'rb')),
            ('files', open('tests/files/file-sample_100kB.docx', 'rb')),
            ('files', open('tests/files/file_example_XLSX_10.xlsx', 'rb')),
            ('files', open('tests/files/tests-example.xls', 'rb')),
            ('files', open('tests/files/SamplePPTFile_500kb.ppt', 'rb')),
            ('files', open('tests/files/samplepptx.pptx', 'rb')),
        ]
    
    
    async with httpx.AsyncClient() as client:
        response = await client.put(url=f"{rl}/{agent_id}/{req}", 
                                    files=files, 
                                    timeout=None)
        if response.status_code == 204:
            return response
        else:
            return {"error": "Failed to extract files", "status_code": response.status_code}

async def extract_websites(agent_id):
    agent_id = agent_id
    rl = "http://localhost:8000/agents" 
    req = "websites"

    
    websites = {
       "urls": [
            "https://www.mayoclinic.org/diseases-conditions/lung-cancer/symptoms-causes/syc-20374620",
            "https://www.gleneagles.com.sg/conditions-diseases/lung-cancer/symptoms-causes"
            ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.put(url=f"{rl}/{agent_id}/{req}", 
                                    json=websites,
                                    timeout=None)
        if response.status_code == 204:
            return response
        else:
            return {"error": "Failed to extract websites", "status_code": response.status_code}

async def get_agent(agent_id):
    agent_id = agent_id
    rl = "http://localhost:8000/agents" 
    

    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"{rl}/{agent_id}", 
                                    timeout=None)
        if response.status_code == 200:
            return response.json()  
        else:
            return {"error": "Failed to get agent", "status_code": response.status_code}

async def query_agent(agent_id, query):
    agent_id = agent_id
    rl = "http://localhost:8000/agents" 
    req = "queries"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url=f"{rl}/{agent_id}/{req}", 
                                    json=query,
                                    timeout=None)
        if response.status_code == 201:
            return response.json()  
        else:
            return {"error": "Failed to query agent", "status_code": response.status_code}

async def delete_agent(agent_id):
    agent_id = agent_id
    rl = "http://localhost:8000/agents" 
    

    async with httpx.AsyncClient() as client:
        response = await client.delete(url=f"{rl}/{agent_id}", 
                                    timeout=None)
        if response.status_code == 204:
            return response
        else:
            return {"error": "Failed to delete agent", "status_code": response.status_code}


# Example usage
async def main():
    agent_id = await create_agent_request() #Adding of files and websites is inside here
    agent_id = agent_id['agent_id']
    print(f"agent_id: {agent_id}\n")

    res = await extract_files(agent_id)
    print(f"extract files response: {res}\n")

    res = await extract_websites(agent_id)
    print(f"extract website response: {res}\n")

    query = {'query': "What is cancer?"}

    res = await query_agent(agent_id, query)
    print(f"query agent response: {res}\n")

    res = await get_agent(agent_id)
    print(f"get agent response: {res}\n")
    
    res = await delete_agent(agent_id)
    print(f"delete agent response: {res}\n")

    res = await get_agent(agent_id)
    print(f"get agent response should fail after deleing: {res}\n")


asyncio.run(main())