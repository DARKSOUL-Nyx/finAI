import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def fetch_latest_news(company):
    """Fetch latest finance-related news headlines for a company."""
    url = f"https://news.google.com/search?q={company}%20stock&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    # A list of potential class names for article links
    class_names = ["JtKRv", "DY5T1D", "RZIKme"]

    for class_name in class_names:
        for item in soup.find_all("a", class_=class_name)[:8]:
            headline = item.text
            link = "https://news.google.com" + item['href'][1:]
            articles.append({"headline": headline, "url": link})
        if articles:  # If articles are found, break the loop
            break

    # Save news data
    with open("data/news_data.json", "w") as f:
        json.dump({company: articles, "timestamp": str(datetime.now())}, f, indent=2)
    return articles
