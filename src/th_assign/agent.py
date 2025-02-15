import os
from typing import TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import tiktoken


from dotenv import load_dotenv
load_dotenv()


class Agent:
    def __init__(self, tools, model_name, api_key=os.getenv("OPENAI_API_KEY")):
        self.model_name = model_name
        self.model = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=api_key
        )
        self.react_agent = create_react_agent(model=self.model, tools=tools)
        self.sys_msg = '''
            You are a Research Agent whose job is to give detailed explaination to the user question.
            You will be given a context, where you will be using it closely to answer the user question.

            If the context given is EMPTY or NOT RELEVANT to the user question, then you may use the 
            tools provided to you to answer the user question.
            
            Context: {context}
            '''

    def add_tools(self):
        pass

    def tokenize(self, text):
        model_to_encoding_map = {
            "gpt-4o-mini": "o200k_base",
            "gpt-4o": "o200k_base",
            "gpt-4-turbo": "cl100k_base",
            "gpt-4": "cl100k_base",
            "gpt-3.5-turbo": "cl100k_base"
        }
        encoding = tiktoken.get_encoding(model_to_encoding_map[self.model_name])
        num_tokens = len(encoding.encode(text))
        return num_tokens

    def invoke_agent(self, knowledge_base: str, query: str):
        task_message = "The user question is {query}"
        prt_template = ChatPromptTemplate.from_messages(
            [
                ('system', self.sys_msg),
                ('user', task_message)
            ]
        )
        filled_template = prt_template.format(
                query=query,
                context=knowledge_base
            )
        res = self.react_agent.invoke(
            {"messages": [filled_template]}
        )
        print(res['messages'])
        return res['messages'][-1].content
        
