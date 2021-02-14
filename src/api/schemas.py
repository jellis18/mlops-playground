import datetime
from enum import Enum

from pydantic import BaseModel, Field, confloat


class SentimentType(str, Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"


class Review(BaseModel):
    text: str = Field(..., description="Text from review")
    date: datetime.datetime = Field(datetime.datetime.now(), description="Date of review")


class Sentiment(BaseModel):
    label: SentimentType
    score: confloat(ge=0, le=1)
