import asyncio
from rich.console import Console
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from .config import OPENAI_API_KEY
import time

console = Console()


prompt = ChatPromptTemplate.from_template("You are a trivia master. Answer clearly and concisely:\n\nQuestion: {question}")

model = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-3.5-turbo",
    temperature=0,
    streaming=True
)


parser = StrOutputParser()


chain = prompt | model | parser

def ask_trivia_sync():
    console.print("[bold green]Instant Trivia Bot(sync mode)[/bold green]")
    while True:
        q = console.input("[yellow]❓ Enter trivia question (or 'quit'): [/yellow]")
        if q.strip().lower() in {"quit", "exit"}:
            break
        console.print("[cyan]💡 Answer:[/cyan] ", end="")
        for chunk in chain.stream({"question": q + " Please answer in detail and slowly."}):
            console.print(chunk, end="", style="white")
            time.sleep(0.5)  # 50ms delay so you can *see* it stream
        console.print()


async def ask_trivia_async():
    console.print("[bold green]Instant Trivia Bot (async mode)[/bold green]")
    while True:
        q = console.input("[yellow]❓ Enter trivia question (or 'quit'): [/yellow]")
        if q.strip().lower() in {"quit", "exit"}:
            break
        console.print("[cyan]💡 Answer:[/cyan] ", end="")
        async for chunk in chain.astream({"question": q + " Please answer in detail and slowly."}):
            console.print(chunk, end="", style="white")
            await asyncio.sleep(0.05)  # same delay in async
        console.print()

        # Full answer at once (optional)
        full_answer = await chain.ainvoke({"question": q})
        console.print(f"[dim]Full captured answer: {full_answer}[/dim]")

def main():
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "sync"
    if mode == "async":
        asyncio.run(ask_trivia_async())
    else:
        ask_trivia_sync()