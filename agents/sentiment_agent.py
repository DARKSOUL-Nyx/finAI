# from transformers import pipeline
# import requests
# from bs4 import BeautifulSoup

# sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

# def fetch_financial_news(company):
#     url = f"https://news.google.com/search?q={company}%20stock&hl=en-IN&gl=IN&ceid=IN:en"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     headlines = [h.text for h in soup.find_all("a", class_="JtKRv")]
#     return headlines[:5]

# def analyze_sentiment(headlines):
#     results = sentiment_analyzer(headlines)
#     avg_score = sum([r['score'] if r['label'] == 'positive' else -r['score'] for r in results]) / len(results)
#     sentiment_label = "Positive" if avg_score > 0 else "Negative"
#     return sentiment_label, avg_score

from transformers import pipeline
import json

sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_news_sentiment():
    try:
        with open("data/news_data.json", "r") as f:
            headlines = json.load(f)
        results = sentiment_analyzer(headlines)
        avg_score = sum([
            r['score'] if r['label'] == 'positive' else -r['score']
            for r in results
        ]) / len(results)
        sentiment_label = "Positive" if avg_score > 0 else "Negative"
        return sentiment_label, avg_score
    except Exception as e:
        return "Neutral", 0.0
