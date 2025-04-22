from fastapi import FastAPI, Request
from agent import run_agent

app = FastAPI()

from tools.stock_fetcher import get_stock_price
print(get_stock_price("AAPL"))


@app.post("/query")
async def query_agent(request: Request):
    data = await request.json()
    query = data.get("query", "")
    response = run_agent(query)
    return {"response": response}
