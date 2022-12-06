import streamlit as st
import requests
import json
import sys
import yfinance as yf
import pandas as pd
import altair as alt

st.set_page_config(page_title="Stock Analysis")

# FastAPI endpoints for add and delete stocks
backend = "http://backend:8080/"

st.title("Stocks Screening & Analysis")

st.sidebar.image("http://i.ibb.co/W0kCzkV/stock-market-icon-png-28.png", width=100,
                channels='BGR', output_format='PNG')

st.sidebar.header("Stocks Screening & Analysis")
with st.sidebar.expander("Info"):
    st.info(f"""
        Click [here](https://finance.yahoo.com/trending-tickers/)
        for a list of trending stock tickers on Yahoo Finance.
        """)
st.sidebar.checkbox("Show historical prices chart", value=True,key="sideBr")
user_hist_period = st.sidebar.selectbox(
            "Select a period", ['1mo', '3mo', '6mo', '1y']
            )
df = pd.DataFrame()
#imput for stocks volume history
form = st.form(key='my_form')
form.text_input(label='Enter Stocks Symbole for history', key="name")
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    response = requests.get(f"{backend}stocks/{st.session_state.name}").json()
    stocks =  response['stocks']
    df = pd.DataFrame(stocks, columns=[
                     'Date','Open', 'High', 'Low', 'Close', 'Volume'],dtype = float)

    table = st.write(df)
    reset_button = form.form_submit_button(label='Reset')
    if reset_button:
        table.write()
    if df.shape[0]!=0:
        if st.session_state.sideBr:
            # call yfinance API for historical data of selected ticker
            hist = yf.Ticker(st.session_state.name).history(period=user_hist_period)
            hist_mini = hist[['Close', 'Volume']].reset_index()
            hist_mini['Volume'] = hist_mini['Volume'].apply(lambda x : x/1000000)

            # build due-axis chart showing volume and price history
            base = alt.Chart(hist_mini).encode(x='Date')
            bar = base.mark_bar(color='#5276A7').encode(
                        alt.Y('Volume', axis=alt.Axis(title='Volume (million)',
                                titleColor='#5276A7')))

            line = base.mark_line(color='red').encode(
                        alt.Y('Close', axis=alt.Axis(title='Price (USD)',
                                titleColor='red')))

            # # https://altair-viz.github.io/gallery/layered_chart_with_dual_axis.html
            c1 = alt.layer(bar, line).resolve_scale(y = 'independent')
            st.altair_chart(c1, use_container_width=True)
form_twit = st.form(key='my_form_twit')
form_twit.text_input(label='Enter Stocks Name for twits', key="name_for_twit")
submit_twit = form_twit.form_submit_button(label='Submit')
if submit_twit:
    twins = requests.get(f"{backend}twins/{st.session_state.name_for_twit}").json()
    if twins["share"] == "no tweets":
        df = pd.DataFrame([],columns=[
                     'tweet'],dtype = str)
    else:
        tweet =  twins['tweet']
        df = pd.DataFrame(tweet, columns=[
                        'tweet'],dtype = str)
    table = st.write(df)

form_analysis = st.form(key='my_form_analysis')
form_analysis.text_input(label='Enter Stocks Name for Analysis', key="name_for_analysis")
submit_analysis = form_analysis.form_submit_button(label='Submit')
if submit_analysis:
    analysis = requests.get(f"{backend}analysis/{st.session_state.name_for_analysis}").json()
    st.header("Twitts Analysys! :heart:  :nerd_face:")
    st.latex(f"positive : {analysis['positive']}, negative: {analysis['negative']}")