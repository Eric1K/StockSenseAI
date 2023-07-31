import pandas as pd
from pandas_datareader import data #as pdr

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

from time import sleep

from prophet import Prophet

import yfinance as yf

import mplfinance as mpf

from lightweight_charts import Chart


#from datetime import datetime

#import plotly.io as pio
#pio.renders.default='colab'

#todo: yahoo finance, automatically download CSV historical data

#df = pd.read_csv("SPY.csv")

#df = pdr.get_data_yahoo("SPY", start="2022-07-30", end="2023-07-30")

def openChart(df, stock, start, end, period, interval):
    chart = Chart()
    chart.set(df)    
    chart.show()
    chart.marker(text='Start')

    enddate = pd.to_datetime(end) + pd.DateOffset(days=period)
    enddate = enddate.date()


    #backtest ticker
    tickertemp = yf.download(stock, start=end, end=enddate, interval=interval)
    tickertemp.to_csv("backtestdata.csv")
    df2 = pd.read_csv("backtestdata.csv")

    
    for i, series in df2.iterrows():
        chart.update(series)
        sleep(0.1)

    chart.marker(text='End')
    chart.show(block = True)
        
        #mpf.plot(ticker, type="candle", ylabel = "Price (USD)", volume = True, style = "yahoo")

        #def graph_data(stock):
            #print("hi")
            #start = "01-01-2017"
            #end = ("01-01-2019")
            #cd = data.DataReader(stock, 'yahoo', start=start)
            #print(cd.head())
        # mpf.plot(df, type="candle", ylabel = "Price", title = "Data", volume = True, style="yahoo")

        #graph_data("FB")

        #chart = px.line(df, x="Date", y="Close"), box, bar

        #futuregraph = px.line(prediction, x='ds', y='yhat')

        #futuregraph = p.plot(prediction, xlabel='ds', ylabel='y')
        #futuregraph.show()


def graph(stock, start, end, period, interval):
    ticker = yf.download(stock, start=start, end=end, interval=interval)
    ticker.to_csv("tickerdata.csv")
    df = pd.read_csv("tickerdata.csv")
    #print(df)
    #print(df.describe())

    #predict using prophet ML
    columns = ['Date', 'Close']
    ndf = pd.DataFrame(df, columns=columns)
    prophet_df = ndf.rename(columns={'Date':'ds', 'Close':'y'})

    p = Prophet(daily_seasonality = True)
    p.fit(prophet_df)

    future = p.make_future_dataframe(periods=period)
    prediction = p.predict(future)
    #print(prediction)

    #show chart of prediction
    from prophet.plot import plot_plotly
    graph2 = plot_plotly(p, prediction, figsize=(1600,900))
    graph2.update_layout(
        title="Prediction",
    )

    from plotly.offline import plot
    plot(graph2)
    #graph2.show()

    #show candlestick chart
    openChart(df, stock, start, end, period, interval)
    
    """chart = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    chart.update_layout(
        title='Dataset'
    )
    chart.show()"""


#graph(TICKER, START DATE, END DATE, HOW FAR THE PREDICTION, TIME INTERVAL)
if __name__ == '__main__':
    graph("SPY", "2021-6-01", "2023-5-30", 300, "1d")

