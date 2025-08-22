from pydantic.v1 import BaseModel
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI, OpenAIEmbeddings

class AnswerSchema(BaseModel):
    answer: str
    source: str

retriever = Chroma.from_documents(docs, OpenAIEmbeddings()).as_retriever()
llm = OpenAI()

# This looks valid but fails
chain = retriever | llm.with_structured_output(AnswerSchema)
result = chain.invoke("What is LangChain?")


# ValidationError: Expected type `AnswerSchema`, got `str`
