from pydantic.v1 import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI, OpenAIEmbeddings


class AnswerSchema(BaseModel):
    answer: str
    source: str

prompt = PromptTemplate.from_template(
    "Use the following context to answer the question:\n{context}\n\nQ: {question}\nA:"
)

retriever = Chroma.from_documents(docs, OpenAIEmbeddings()).as_retriever()
llm = OpenAI(model="gpt-4o", json_mode=True)

chain = (
    retriever
    | (lambda docs: {"context": "\n".join([d.page_content for d in docs]), "question": "What is LangChain?"})
    | prompt
    | llm.with_structured_output(AnswerSchema, method="json_mode")
)

result = chain.invoke("What is LangChain?")
