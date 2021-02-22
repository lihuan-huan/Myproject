import json
import time

import numpy as np
import pandas as pd
import tushare as ts

def pro_daily_stock(code_val='', start_val='20180101', end_val='20210101'):
    # 获取股票日线行情数据
    df_stock = pro.daily(ts_code=code_val, start_date=start_val, end_date=end_val)
    df_stock.trade_date = pd.DatetimeIndex(df_stock.trade_date)
    df_stock.set_index("trade_date", drop=True, inplace=True)
    df_stock.sort_index(inplace=True)
    df_stock.index = df_stock.index.set_names('Date')

    recon_data = {'ts_code': code_val, 'High': df_stock.high, 'Low': df_stock.low, 'Open': df_stock.open, 'Close': df_stock.close,\
                  'Volume': df_stock.vol}
    df_recon = pd.DataFrame(recon_data)

    return df_recon

# print(ts.get_hist_data('hs300'))#data = ts.get_hs300s()
pro = ts.pro_api('2356036d2a6c009eb07b649eee0bb123226b24251eedea2235a6de1f')

data = pro.stock_basic()

j = 0
for inx, i in data.iterrows():

    print(i['ts_code'])
    #df = pro.daily(ts_code=i['ts_code'], start_date='20200701', end_date='20200718')
    #ts_code     trade_date  open  high   low  close
    pro_daily_stock(i['ts_code']).to_json("Historical_transaction_data.json")
    time.sleep(0.1)



