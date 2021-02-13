from fastapi import FastAPI
from transformers import pipeline

from .schemas import Sentiment, Review

app = FastAPI(description="Sentiment Analysis with Huggingface")

model = pipeline("sentiment-analysis")


@app.post("/predict", response_model=Sentiment)
async def predict(review: Review) -> Sentiment:
    """
    Predict the sentiment of a review.
    """
    pred = model(review.text)[0]
    return Sentiment(label=pred["label"].lower(), score=pred["score"])
