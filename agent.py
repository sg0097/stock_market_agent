from langchain.agents import initialize_agent, Tool
from langchain_ollama import OllamaLLM  # updated import
from tools.stock_fetcher import get_stock_price

llm = OllamaLLM(model="llama3")

tools = [
    Tool(
    name="StockFetcher",
    func=get_stock_price,
    description="Gets the current stock price and buy/sell/hold recommendation for a given stock ticker. Input should be a ticker symbol like AAPL, TSLA, or GOOG."
)

]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_agent(query: str) -> str:
    return agent.run(query)
