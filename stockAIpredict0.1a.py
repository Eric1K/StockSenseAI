import pandas as pd
from pandas_datareader import data #as pdr

import plotly.express as px
import plotly.graph_objects as go


from prophet import Prophet

import yfinance as yf

import mplfinance as mpf

#from datetime import datetime

#import plotly.io as pio
#pio.renders.default='colab'

#todo: yahoo finance, automatically download CSV historical data

#df = pd.read_csv("SPY.csv")

#df = pdr.get_data_yahoo("SPY", start="2022-07-30", end="2023-07-30")
ticker = yf.download("SPY", start="2021-07-30", end="2023-07-30")
ticker.to_csv("TickerData.csv")
df = pd.read_csv("TickerData.csv")

print(df)
print(df.describe())

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
chart = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
chart.update_layout(
    title='Dataset'
)
chart.show()


columns = ['Date', 'Close']
ndf = pd.DataFrame(df, columns=columns)
prophet_df = ndf.rename(columns={'Date':'ds', 'Close':'y'})

p = Prophet(daily_seasonality = True)
p.fit(prophet_df)

future = p.make_future_dataframe(periods=1000)
prediction = p.predict(future)

print(prediction)

#futuregraph = px.line(prediction, x='ds', y='yhat')

#futuregraph = p.plot(prediction, xlabel='ds', ylabel='y')
#futuregraph.show()

from prophet.plot import plot_plotly, plot_components_plotly
graph2 = plot_plotly(p, prediction, figsize=(1600,900))
graph2.update_layout(
    title="Prediction",
)
graph2.show()