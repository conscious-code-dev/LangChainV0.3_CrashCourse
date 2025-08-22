from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt = PromptTemplate.from_template("Q: {q}\nA:")
llm = OpenAI()

chain = prompt | llm 

response = chain.invoke({"q": "What is WebAssembly?"})
print(response)


