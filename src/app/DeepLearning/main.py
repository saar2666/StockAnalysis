from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
import asyncio
from transformers import pipeline
import pandas as pd
import requests
import re
import json
asyncio.set_event_loop(asyncio.new_event_loop())



def text_analysis(data:pd):
    #Removing RT, Punctuation etc
    remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
    rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([0-9A-Za-z \t])|(\w+:\/\/\S+)","" "",x)
    data["tweet"] = data.tweet.map(remove_rt).map(rt)
    data["tweet"] = data.tweet.str.lower()
    classifier = pipeline("text-classification")
    classifier = pipeline("sentiment-analysis",model ="distilbert-base-uncased-finetuned-sst-2-english")
    for index, row in data["tweet"].iteritems():
        data.loc[index, "sentimment"] = classifier(row)[0].get("label")
    total=data.loc[:,"sentimment"].value_counts(dropna=False)
    print(total["NEGATIVE"])
    print(total["POSITIVE"])
    return {"negative":int(total["NEGATIVE"]),"positive":int(total["POSITIVE"])}

@dataclass
class TweetResponse:
    share: str
    tweet: List[str]

class StockRequest(BaseModel):
    ticker: str

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "hello from DeepLearning"}


@app.get("/analysis/{search}")
def get_analysis(search):
    response = requests.get(f"http://twitter:9090/twins/{search}").json()
    tweet =  response['tweet']
    df = pd.DataFrame(tweet, columns=[
                        'tweet'],dtype = str)
    print(df.head())
    data = text_analysis(df)
    return data
