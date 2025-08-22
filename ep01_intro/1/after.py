

from pydantic.v1 import BaseModel, Field 
from langchain_openai import OpenAI

class ReportSummary(BaseModel):
    revenue: float = Field(...)
    profit_margin: float = Field(...)

llm = OpenAI() # Optionally set model="gpt-3.5-turbo"

structured_llm = llm.with_structured_output(ReportSummary)

result = structured_llm.invoke("Summarize Q2 earnings of Apple Inc.")

print(result)

formatted_text = {
    "revenue": 5200000.00, 
    "profit_margin": 2000000.00
    }