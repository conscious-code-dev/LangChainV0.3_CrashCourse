from fastapi.testclient import TestClient
from src.contract_simplifier.api.main import app

client = TestClient(app)

def test_simplify_contract():
    res = client.post("/simplify", json={"contract_text": "This contract is binding..."})
    assert res.status_code == 200
    assert "simplified_text" in res.json()
