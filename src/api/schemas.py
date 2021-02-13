import datetime
from enum import Enum

from pydantic import BaseModel, confloat


class SentimentType(str, Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"


class Review(BaseModel):
    text: str
    date: datetime.datetime = datetime.datetime.now()


class Sentiment(BaseModel):
    label: SentimentType
    score: confloat(ge=0, le=1)
