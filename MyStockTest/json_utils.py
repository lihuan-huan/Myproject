import json
import tushare as ts
index = {'上证综指': 'sh.000001',
            '深证成指': 'sz.399001',
            '沪深300': 'sh.000300',
            '上证50': 'sh.000016'}


pro = ts.pro_api('2356036d2a6c009eb07b649eee0bb123226b24251eedea2235a6de1f')
df = pro.stock_basic(exchange='',list_status='L')
codes = df.ts_code.values
names = df.name.values
stock=dict(zip(names, codes))

stock_index = dict([('指数', index),('股票', stock)])

with open("stock_pool.json", "w", encoding='utf-8') as f:
    json.dump(stock_index, f, ensure_ascii=False, indent=4)

def open_json():
    with open("stock_pool.json", "r") as f:
        stock_t = json.load(f)
    print(stock_t)
