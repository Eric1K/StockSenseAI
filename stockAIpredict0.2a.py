import pandas as pd
from pandas_datareader import data #as pdr

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.offline import plot

from datetime import datetime
from time import sleep
from prophet import Prophet
import yfinance as yf
import mplfinance as mpf
from lightweight_charts import Chart
import eel



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
        

@eel.expose
def graph(stock, start, end, period, interval, graphCandles):
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
        title= "$" + stock + " Prediction for " + end,
    )

    from plotly.offline import plot
    plot(graph2)
    #graph2.show()

    #show candlestick chart
    if graphCandles == "True":
        openChart(df, stock, start, end, period, interval)
    



#graph(TICKER, START DATE, END DATE, HOW FAR THE PREDICTION, TIME INTERVAL)
if __name__ == '__main__': 
    eel.init('web')

    """@eel.expose
    def dummy(dummy_param):
        print("helloworld: ", dummy_param)
        return "string_value", 1, 1.2, True, [1,2,3,4], {"name":"eel"}
    """

    eel.start("index.html", size=(1240,830))

    #GRAPH
    #graph("SPY", "2021-6-01", "2023-5-30", 100, "1d", True)
    
    print("done")
