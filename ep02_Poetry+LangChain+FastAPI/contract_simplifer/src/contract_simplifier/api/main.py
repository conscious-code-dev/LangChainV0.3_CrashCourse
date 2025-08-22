from fastapi import FastAPI
from pydantic import BaseModel
from src.contract_simplifier.chains.simplify_contract import contract_simplifier_chain
import uvicorn


class ContractRequest(BaseModel):
    contract_text:str

app = FastAPI()



@app.get("/health")
def health_check():
    return {"status":"okay"}


@app.post("/simplify")
def simplify_contract(req:ContractRequest):
    output = contract_simplifier_chain.invoke({"contract_text":req.contract_text})

    return {"simplified_text":output.content}


def run():
    uvicorn.run("src.contract_simplifier.api.main:app",host="127.0.0.1", port=8000,reload=True)