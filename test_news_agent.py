import sys
from agents.news_agent import fetch_latest_news

if len(sys.argv) > 1:
    ticker = sys.argv[1]
else:
    ticker = "AAPL"

articles = fetch_latest_news(ticker)
print(articles)