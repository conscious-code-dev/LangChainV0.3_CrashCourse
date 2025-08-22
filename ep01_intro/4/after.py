from langchain.agents import create_react_agent,AgentExecutor,Tool
from langchain_openai import OpenAI

tools = [
    Tool(name="Weather", func=get_weather, description="Get weather"),
    Tool(name="Calendar", func=list_events, description="List events"),
]

llm = OpenAI()
react_agent = create_react_agent(llm, tools)
executor = AgentExecutor(agent=react_agent, tools=tools)

response = executor.invoke({"input": "What's the weather and my meetings today?"})
