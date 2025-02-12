import os

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()

class Agent:
    def __init__(self, model_name, api_key=os.getenv("OPENAI_API_KEY")):
        self.model = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=api_key
        )

        self.react_agent = create_react_agent(model=self.model, tools=[])

    def add_tools(self):
        pass

    def invoke_agent(self, query, *args):
        pass
