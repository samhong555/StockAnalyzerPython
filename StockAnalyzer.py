import pandas as pd
from datetime import datetime, timedelta
import talib
import matplotlib
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data

"""Path Files and other variables"""
stocks_file = 'input/stock.txt'
today_date = datetime.today()
prior_2 = today_date - timedelta(2)

"""Get private token key"""
with open('token.txt') as t:
    tlines = t.read().replace('/n', '')
token_key = tlines
print(token_key)


"""Get stock ticker list"""
with open(stocks_file) as f:
    lines = f.read().splitlines()
stock_list = lines
print(stock_list)
#master_stock_list = Stock(stock_list, token='pk_0ddf122dbf914d84b585a8d64212a7ef')

"""API for Stock Data """

df_all_historical_daily = pd.DataFrame()
for stock in stock_list:
    df_temp_historical_daily = get_historical_data(stock,prior_2,today_date,output_format='pandas',token=token_key)
    df_temp_historical_daily['symbol'] = stock
    df_all_historical_daily = df_all_historical_daily.append(df_temp_historical_daily)

#df_all_historical_daily = get_historical_data(stock_list,prior_2,today_date,output_format='pandas',token='pk_0ddf122dbf914d84b585a8d64212a7ef')
df_all_historical_daily['date'] = df_all_historical_daily.index
print(df_all_historical_daily)


"""Store in Database - Postgresql"""
df_all_historical_daily.to_csv('/Users/samhong/Desktop/data_dump.csv',index=False)



"""Perform TA"""





"""Email List Out"""