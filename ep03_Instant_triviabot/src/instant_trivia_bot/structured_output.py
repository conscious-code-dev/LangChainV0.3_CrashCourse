from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from .config import OPENAI_API_KEY

class TriviaAnswer(BaseModel):
    question: str = Field(description="The trivia question asked")
    answer: str = Field(description="The concise answer in one sentence")

def run_structured_demo():
    parser = JsonOutputParser(pydantic_object=TriviaAnswer)

    prompt = ChatPromptTemplate.from_template("""
    Answer the following trivia question as JSON strictly following the schema:
    {format_instructions}

    Question: {question}
    """)

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,api_key=OPENAI_API_KEY)

    chain = prompt | model | parser

    result = chain.invoke({
        "question": "What is the capital of Japan?",
        "format_instructions": parser.get_format_instructions()
    })

    print(result)

if __name__ == "__main__":
    run_structured_demo()
