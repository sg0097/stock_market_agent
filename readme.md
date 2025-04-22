# 📈 Stock Market AI Agent

This project creates an AI-powered API using **LangChain**, **Ollama**, **FastAPI**, and **yfinance** that:
- Fetches current stock prices.
- Gives buy/sell/hold recommendations.
- Understands natural language queries.

---

## ⚙️ Technologies Used

- **Python 3.8+**
- **LangChain**
- **FastAPI**
- **Ollama** (for local LLM like LLaMA 3)
- **yfinance** (stock data fetcher)

---

## 🗂️ Project Structure

```
.
├── main.py           # FastAPI app
├── agent.py          # LangChain agent setup
├── requirements.txt  # Python dependencies
├── README.md
```

---

## 🔧 Setup Instructions

### 1. Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) (must be installed and running)

### 2. Install Ollama Model

```bash
ollama run llama3
```

Keep this running in a terminal. It loads the LLM.

---

### 3. Clone This Repo

```bash
git clone <your-repo-url>
cd stock-ai-agent
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the FastAPI App

```bash
python main.py
```

Your backend will start at: `http://localhost:8000`

---

### 6. Test the API

Use these sample `curl` calls:

#### ✅ Get Stock Price
```bash
curl -X POST http://localhost:8000/query \
-H "Content-Type: application/json" \
-d "{\"query\": \"What is the price of AAPL stock?\"}"
```

#### ✅ Get Buy/Sell Recommendation
```bash
curl -X POST http://localhost:8000/query \
-H "Content-Type: application/json" \
-d "{\"query\": \"Should I buy or sell TSLA stock?\"}"
```

#### ✅ Sample Response
```json
{
  "response": "You should buy TSLA stock based on recent price trends and averages."
}
```

---

## 🧠 How It Works

- User query → LangChain agent → yfinance fetches real stock data
- LLM (LLaMA 3 via Ollama) processes it and responds naturally
- Example logic:
  - Compares current price to 5-day moving average
  - Makes decision: Buy / Sell / Hold

---

## 🌍 Deploying to Render

1. Push code to GitHub
2. Go to [https://render.com](https://render.com), create new Web Service
3. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 8000`
4. Connect Ollama (on same server or locally)

---

## 🧾 requirements.txt

```text
fastapi
uvicorn
langchain
yfinance
requests
pydantic
```

---

## 📜 License

MIT License — use, modify, and distribute freely.

---

## 🙌 Credits

Made with:
- LangChain
- Ollama
- FastAPI
- yfinance
