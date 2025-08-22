from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0.0,
    max_tokens=1024
)

SYSTEM_PROMPT = "You are a legal assistant that simplifies legal contracts into plain language anyone can understand."

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{contract_text}")
])

contract_simplifier_chain = prompt | llm


print(contract_simplifier_chain.invoke({
    "contract_text":"The lessee shall indemnify the lessor..."
}).content)
