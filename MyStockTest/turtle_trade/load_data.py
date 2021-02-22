import json
import numpy as np
import pandas as pd
import tushare as ts

def open_json(dir):
    with open(dir, "r") as f:
        stock_t = json.load(f)
    print(stock_t)

#open_json('Historical_transaction_data.json')
df = pd.read_json('Historical_transaction_data.json')


print(df.head())