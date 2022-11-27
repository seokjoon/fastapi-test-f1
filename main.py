# Press Shift+F10 to execute it or replace it with your code.

from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
# def read_root():
async def read_root():
    return {'hello': 'world'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


# async def run():
#     import dc_api
#     print('run')
#     async with dc_api.API() as api:
#         async for index in api.board(board_id='stockus', num=10, start_page=1):
#             print(index.title)
#             # break
#     return None
#
#
# @app.get('/bar')
# def bar():
#     import asyncio
#     asyncio.run(run())
#     return None


@app.get('/foo')
def foo():
    try:
        # import json
        # print(json.loads('{"foo": "bar"}'))

        # import FinanceDataReader as fdr
        # df = fdr.__version__
        # df = fdr.DataReader('US2YT=X').head()
        # df = fdr.DataReader('AAPL', '2022-10-6', '2022-10-7').tail()
        # df = fdr.StockListing('KRX').head()
        # df = fdr.DataReader('DJI')

        import pandas_datareader as pdr
        # import yfinance as yf
        # yf.pdr_override()
        df = pdr.__version__
        import datetime
        # print(datetime.datetime(2022, 10, 6, 10, 10, 10))
        # df = pdr.get_data_fred("GS2", datetime.datetime(2022, 10, 6), datetime.datetime(2022, 10, 7))
        # from pandas_datareader.fred import FredReader
        # df = FredReader('GS2').read()
        start = datetime.datetime(2022, 10, 7, 4, 10, 1)
        # start = datetime.datetime(2022, 10, 6)
        stop = datetime.datetime(2022, 10, 8, 4, 10, 1)
        # stop = datetime.datetime(2022, 10, 7)
        # df = pdr.DataReader('GS2', 'fred', start, stop)
        # df = pdr.get_data_yahoo("VPU", start="2022-10-07", end="2022-10-07").head()
        # df = pdr.get_data_yahoo("^GSPC", start="2022-10-07", end="2022-10-07")
        # df = pdr.DataReader('^FVX', 'yahoo', start, stop)
        # df = pdr.DataReader('005930', 'naver', start='2022-10-06', end='2022-10-07')
        import pandas_datareader.data as web
        df = web.DataReader('AAPL', 'av-intraday', start=start, end=stop, api_key='')
        print(df.tail())

        # import requests
        # url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=2year&apikey='
        # r = requests.get(url)
        # data = r.json()
        # print(data)

        df = ''
    except Exception as e:
        print(e)

    # fdr.chart.plot(df)

    return {'foo': df}