import plotly.graph_objects as go
import plotly.subplots as ms
import FinanceDataReader as fdr
import pandas as pd
import talib

df = fdr.DataReader('BTC/KRW', '2020-02-01')

# DataFrame에 이동평균값 추가하기
df['MA5'] = talib.SMA(df['Close'], timeperiod=5)
df['MA20'] = talib.SMA(df['Close'], timeperiod=20)
df['MA60'] = talib.SMA(df['Close'], timeperiod=60)
df['MA120'] = talib.SMA(df['Close'], timeperiod=120)

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

# 이동평균선 생성
ma5 = go.Scatter(x=df.index, y=df['MA5'], line=dict(color='black', width=0.8), name='ma5')
ma20 = go.Scatter(x=df.index, y=df['MA20'], line=dict(color='red', width=1), name='ma20')
ma60 = go.Scatter(x=df.index, y=df['MA60'], line=dict(color='green', width=0.9), name='ma60')

# 바 차트(거래량) 객체 생성
# volume_bar = go.Bar(x=df.index, y=df['Volume'])
# fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
# fig.add_trace(candlestick, row=1, col=1)
# fig.add_trace(volume_bar, row=2, col=1)

# 첫번째 행에 캔들차트를 추가하고 그 다음으로 거래량 차트를 추가한다.
# fig.update_layout(title='BitCoin stock price',
#                   yaxis1_title='Stock Price',
#                   yaxis2_title='Volume',
#                   xaxis2_title='Periods',
#                   xaxis1_rangeslider_visible=False,
#                   xaxis2_rangeslider_visible=True)

# Create a plot
fig = go.Figure(data=[candlestick, ma5, ma20, ma60])
fig.update_layout(title=dict(text='비트코인 일 차트', x=0.5))
# Show the Plot
fig.show()