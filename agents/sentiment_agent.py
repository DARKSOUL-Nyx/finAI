from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiment(headlines):
    if not headlines:
        return "Neutral", 0.0

    texts = [h["headline"] for h in headlines]
    results = sentiment_pipeline(texts)
    
    avg_score = sum(
        (r["score"] if r["label"] == "positive" else -r["score"]) for r in results
    ) / len(results)

    sentiment = "Positive" if avg_score > 0 else "Negative"
    return sentiment, round(avg_score, 3)
