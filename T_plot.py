import plotly.graph_objects as go
import plotly.subplots as ms
import FinanceDataReader as fdr
import pandas as pd
import talib

df = fdr.DataReader('BTC/KRW', '2020-02-01')

# Define the candlestick
candlestick = go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    increasing_line_color='red', # 양봉 color
    decreasing_line_color='blue'  # 음봉 color
)

# 바 차트(거래량) 객체 생성
volume_bar = go.Bar(x=df.index, y=df['Volume'])
fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
fig.add_trace(candlestick, row=1, col=1)
fig.add_trace(volume_bar, row=2, col=1)

# 첫번째 행에 캔들차트를 추가하고 그 다음으로 거래량 차트를 추가한다.
fig.update_layout(title='BitCoin stock price',
                  yaxis1_title='Stock Price',
                  yaxis2_title='Volume',
                  xaxis2_title='Periods',
                  xaxis1_rangeslider_visible=False,
                  xaxis2_rangeslider_visible=True)

# Create a plot
# fig = go.Figure(data=[candlestick])
# Show the Plot
fig.show()