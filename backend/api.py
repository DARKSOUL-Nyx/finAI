# backend/api.py
from fastapi import FastAPI, HTTPException
from agents.data_agent import fetch_stock_data
from agents.news_agent import fetch_latest_news
from agents.sentiment_agent import analyze_sentiment
from agents.decision_agent import agentic_response
from backend.models import calculate_portfolio_distribution
import pandas as pd

app = FastAPI(title="finAI Backend")

@app.get("/stock_data/{ticker}/{period}")
def get_stock_data(ticker: str, period: str):
    stock_data = fetch_stock_data(ticker, period)
    if stock_data.empty:
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")
    return stock_data.to_json(orient="split")

@app.get("/analyze/{ticker}/{risk}")
def analyze_stock(ticker: str, risk: str, budget: float = 10000, user_message: str = "", chat_history: list = [], latest_price: float = 0.0):
    # 1) headlines & sentiment
    headlines = fetch_latest_news(ticker)
    sentiment_label, sentiment_score = analyze_sentiment(headlines)

    # 2) portfolio suggestion (simple)
    portfolio = calculate_portfolio_distribution(budget, risk)

    # 3) LLM-driven reasoning / advice
    advice = agentic_response(
        user_message=user_message,
        ticker=ticker,
        portfolio=portfolio,
        sentiment_label=sentiment_label,
        sentiment_score=sentiment_score,
        risk_level=risk,
        latest_price=latest_price,
        market_notes="Headlines frequency indicates moderate coverage.",
        chat_history=chat_history,
        headlines=headlines
    )

    return advice
