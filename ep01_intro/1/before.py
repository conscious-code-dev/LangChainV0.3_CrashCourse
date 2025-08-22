

from pydantic import BaseModel
from langchain import OpenAI

class ReportSummary(BaseModel):
    revenue: float
    profit_margin: float


text = " The revenue of the current financial year is 52 Lakhs , The profit margin is 20 Lakhs"

formatted_text = {
    "revenue": 5200000.00, 
    "profit_margin": 2000000.00
    }

llm = OpenAI()

structured_llm = llm.with_structured_output(ReportSummary)

result = structured_llm.run("Summarize Q2 earnings of Apple Inc.")

print(result)




# TypeError: BaseModel.validate() takes 2 positional arguments but 3 were given