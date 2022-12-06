from typing import List
from fastapi import FastAPI
from pydantic.dataclasses import dataclass
from dataclasses import asdict
import requests
import yfinance as yf
import json
import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())




@dataclass
class TweetResponse:
    share: str
    tweet: List[str]

app = FastAPI()

@app.get("/stocks/{stock}")
def get_stocks_table(stock):
    """
    Reads the stocks table from the sqlite database.
    """
    yahoo_data = yf.Ticker(stock)
    data = yahoo_data.history()
    data['Date'] = data.index
    stock_table = {
        "Date": data["Date"].astype(str).tolist(),
        "Open": data["Open"].astype(str).tolist(),
        "High": data["High"].astype(str).tolist(),
        "Low": data["Low"].astype(str).tolist(),
        "Close": data["Close"].astype(str).tolist(),
        "Volume": data["Volume"].astype(str).tolist()
    }
    return{"stocks": stock_table}#stock_table}
    
@app.get("/")
async def read_root():
    return {"Hello": "hello from backend"}


@app.get("/twins/{search}")
def get_twiter(search):
    response = requests.get(f"http://twitter:9090/twins/{search}").json()
    try:
        model = TweetResponse(share=search,tweet = response["tweet"])
        return asdict(model)
    except:
        return {f"share":"no tweets"}


@app.get("/analysis/{search}")
def get_analysis(search):
    response = requests.get(f"http://textanalysis:7070/analysis/{search}").json()
    #moc servise response with twits analysis as positive and negativ posts
    data = {"stock": search, "positive": int(response["positive"]),"negative": int(response["negative"])}
    return data
