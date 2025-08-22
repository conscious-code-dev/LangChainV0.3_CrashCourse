import asyncio
from rich.console import Console
from rich.text import Text
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from .config import OPENAI_API_KEY

console = Console()
prompt = ChatPromptTemplate.from_template("{question}")
model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", streaming=True)
parser = StrOutputParser()

chain = prompt | model | parser


questions = [
    "What is the capital of Iceland?",
    "What is the tallest mountain in Africa?",
    "Who painted the Mona Lisa?",
    "When did WW2 happen?"
]

COLORS = ["cyan" , "magenta", "yellow","green"]
async def ask_question(label,question,color):
    console.print(f"[{color}]{label} Asking {question}[/{color}]")
    console.print(f"[{color}]{label} Answer :[/{color}]")

    async for chunk in chain.astream({"question":question}):
        console.print(Text(chunk , style = color),end="")

async def main():
    tasks = [
        ask_question(f"Q.{i+1}",q, COLORS[i%len(COLORS)])
        for i,q in enumerate(questions)
    ]

    await asyncio.gather(*tasks)


def run():
    import asyncio
    asyncio.run(main())