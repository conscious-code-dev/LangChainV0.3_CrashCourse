from langchain_community.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI

memory = ConversationBufferMemory()
chain = ConversationChain(llm=OpenAI(), memory=memory)

response = chain.invoke({"input": "Hi, I need help with my order."})
print(response)
