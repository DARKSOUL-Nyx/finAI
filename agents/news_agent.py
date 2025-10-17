import requests
from bs4 import BeautifulSoup
import json

def fetch_latest_news(company: str):
    url = f"https://news.google.com/search?q={company}%20stock&hl=en-IN&gl=IN&ceid=IN:en"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    headlines = [h.text for h in soup.find_all("a", class_="JtKRv")]
    json.dump(headlines, open("data/news_data.json", "w"), indent=2)
    return headlines[:5]
