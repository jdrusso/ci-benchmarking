from fastapi.testclient import TestClient
from benchmark.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}, {"column1": 3, "column2": "c"}]