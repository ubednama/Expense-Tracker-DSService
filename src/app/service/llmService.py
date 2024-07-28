from dotenv import load_dotenv, dotenv_values
from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_google_vertexai import ChatVertexAI
from app.schema.Expense import Expense
import os

class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", 
             "You are an expert extraction algorithm."
             "Only extract relevant information from the text."
             "If you do not know the value of an attribute asked to extract"
             "return null for attribute's value"
             ),
             ("human", "{text}")
        ])
        self.apiKey = os.getenv("OPENAI_API_KEY")
        self.llm = ChatMistralAI(api_key=self.apiKey, model="mistral-large-latest", temperature=0)
        # self.llm = ChatOpenAI(temperature=0)
        # self.llm = ChatVertexAI(api_key=self.apiKey, model="gemini-1.5-flash-latest", temperature=0)

        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expense)
    
    def runLLM(self, message):
        return self.runnable.invoke({"text": message})