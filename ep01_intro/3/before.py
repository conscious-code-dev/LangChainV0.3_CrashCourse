from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain import OpenAI

prompt = PromptTemplate.from_template("Q: {q}\nA:")
llm = OpenAI()
chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(q="What is WebAssembly?")
print(response)

# LangChainDeprecationWarning: The class LLMChain was deprecated...
