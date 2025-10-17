# backend/api.py
from fastapi import FastAPI, HTTPException
from agents.data_agent import fetch_stock_data
from agents.news_agent import fetch_latest_news
from agents.sentiment_agent import analyze_news_sentiment
from agents.decision_agent import get_advice_with_reasoning
from backend.models import calculate_portfolio_distribution
import pandas as pd

app = FastAPI(title="finAI Backend")

@app.get("/analyze/{ticker}/{risk}")
def analyze_stock(ticker: str, risk: str, budget: float = 10000):
    # 1) fetch stock data
    stock_data = fetch_stock_data(ticker)
    if stock_data.empty:
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")

    # 2) headlines & sentiment
    headlines = fetch_latest_news(ticker)
    sentiment_label, sentiment_score = analyze_news_sentiment()

    # 3) portfolio suggestion (simple)
    portfolio = calculate_portfolio_distribution(budget, risk)

    # 4) latest price (robust)
    latest_price = None
    try:
        # stock_data expected to have 'Close' column
        latest_price = float(stock_data['Close'].iloc[-1])
    except Exception:
        latest_price = 0.0

    # 5) LLM-driven reasoning / advice
    advice = get_advice_with_reasoning(
        ticker=ticker,
        portfolio=portfolio,
        sentiment_label=sentiment_label,
        sentiment_score=sentiment_score,
        risk_level=risk,
        latest_price=latest_price,
        market_notes="Headlines frequency indicates moderate coverage."
    )

    return {
        "ticker": ticker,
        "sentiment": sentiment_label,
        "score": round(sentiment_score, 3),
        "headlines": headlines,
        "portfolio": portfolio,
        "latest_price": latest_price,
        "advice": advice["raw_text"],
    }
