# Stock Analysing
aplication for stock analysis ,sentiment analysis of twiter posts about stock and stock history (yfinance).
# What in side
service 1 - backend as FastApi  
service 2 - frontend streamlit  
service 3 - twitter , using twin api for gather all twitts for last week  
service 4 - deep learning using huggin face api for analyze text
# Design 
![Alt text](pictures/backend.png?raw=true "Design")

# How to run :
## beckend :
```bash
docker-compose up -d --build  
```
navigat to ```http://localhost:8888/docs```

![](pictures/fastapi.png?raw=true "FastApi")

## response with cloudflare stock:
![Alt text](pictures/search.png?raw=true "Search")
list of last 24 hours twits
# tests :
## integration tests
```bash
docker-compose exec web pytest -m "integration  
```
![](pictures/appVideo.gif "Search")
