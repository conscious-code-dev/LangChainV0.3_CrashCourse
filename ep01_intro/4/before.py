from langchain.agents import initialize_agent, Tool, AgentType
from langchain import OpenAI

tools = [
    Tool(name="Weather", func=get_weather, description="Get weather"),
    Tool(name="Calendar", func=list_events, description="List events"),
]

llm  = OpenAI()
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
response = agent.run("What's the weather and my meetings today?")

# ImportError: cannot import name 'initialize_agent' from 'langchain.agents'
