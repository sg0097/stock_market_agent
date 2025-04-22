import yfinance as yf

def get_stock_price(ticker: str) -> str:
    try:
        ticker = ticker.strip().upper().replace('"', '')  # clean up input
        stock = yf.Ticker(ticker)
        history = stock.history(period="6d")
        
        if history.empty or len(history['Close']) < 2:
            return f"Unable to fetch data for {ticker}. It may be delisted or the symbol is incorrect."

        current_price = history['Close'].iloc[-1]
        last_5_avg = history['Close'].iloc[:-1].mean()

        # Recommendation logic
        if current_price > last_5_avg * 1.02:
            recommendation = "Sell"
        elif current_price < last_5_avg * 0.98:
            recommendation = "Buy"
        else:
            recommendation = "Hold"

        return (
            f"The current price of {ticker} is ${current_price:.2f}. "
            f"The 5-day average was ${last_5_avg:.2f}. Recommendation: {recommendation}."
        )
    except Exception as e:
        return f"Error fetching stock data for {ticker}: {str(e)}"
