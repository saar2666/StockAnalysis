import time, datetime
import twint
import pandas as pd
from fastapi import FastAPI
from pydantic.dataclasses import dataclass
from typing import List
from dataclasses import asdict


@dataclass
class TweetResponse:
    share: str
    tweet: List[str]

def search_twit(search):
    c = twint.Config()
    c.Search = search  # "cloudflare"
    c.Pandas = True
    c.Hide_output = True
    c.Since = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    c.Until = (datetime.date.today()).strftime('%Y-%m-%d')
    twint.run.Search(c)
    try:
        data =  twint.output.panda.Tweets_df[["username", "tweet"]]
        return data
    except:
        return None
app = FastAPI()

@app.get("/")
def get_twiter():
    return {"Hello": "hello from twitte"}

@app.get("/twins/{search}")
def get_twiter(search):
    df =  search_twit(search)
    try:
        model = TweetResponse(share=search,tweet = df["tweet"].tolist())
        return asdict(model)
    except:
        return {f"share":"no tweets"}