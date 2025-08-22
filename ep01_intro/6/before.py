from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI

memory = ConversationBufferMemory()
chain = ConversationChain(llm=OpenAI(), memory=memory)

response = chain.run("Hi, I need help with my order.")
