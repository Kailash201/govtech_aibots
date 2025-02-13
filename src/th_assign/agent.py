import os
from typing import TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


from dotenv import load_dotenv
load_dotenv()

class State(TypedDict):
    query: str
    sys_msg: str
    messages: any
    remaining_steps: any

class Agent:
    def __init__(self, model_name, api_key=os.getenv("OPENAI_API_KEY")):
        self.model = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=api_key
        )

        self.react_agent = create_react_agent(model=self.model, tools=[], state_schema=State)

    def add_tools(self):
        pass

    def invoke_agent(self, query, *args):
        system_message = "You are a research agent whose task is to use appropriate tools if needed to research on a user question"
        task_message = "The user question is {query}"
        prt_template = ChatPromptTemplate.from_messages(
            [
                ('system', system_message),
                ('user', task_message)
            ]
        )
        filled_template = prt_template.format(query=query)
        res = self.react_agent.invoke(
            {"sys_msg": system_message, "query": query, "messages": [filled_template]}
        )
        return res['messages'][-1].content
        


tmp = Agent("gpt-4o-mini")
res = tmp.invoke_agent("hi")
print(res)
