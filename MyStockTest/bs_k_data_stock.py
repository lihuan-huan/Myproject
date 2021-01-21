import baostock as bs
import pandas as pd
#
def bs_k_data_stock(stock, start_date, end_date, freq_val='d', adjust_val='3'):

    lg = bs.login(user_id="anonymous", password="123456")
    fields = "date,open,high,low,close,volume"

    df_bs = bs.query_history_k_data(stock, fields, start_date=start_date, end_date=end_date
                                    , frequency=freq_val, adjustflag=adjust_val)
    data_list = []

    while (df_bs.error_code == '0') & df_bs.next():
            data_list.append(df_bs.get_row_data())


    result = pd.DataFrame(data_list, columns=df_bs.fields)
    result.close = result.close.astype('float64')
    result.open = result.open.astype('float64')
    result.low = result.low.astype('float64')
    result.high = result.high.astype('float64')
    result.volume = result.volume.astype('int')
    result.volume = result.volume/100
    result.index = pd.to_datetime(result.date)
    result.set_index("date", drop=True, inplace=True)

    recon_data = {'High': result.high, 'Low': result.low, 'Open': result.open, 'Colse': result.close
                  , 'Volume': result.volume}
    df_recon = pd.DataFrame(recon_data)
    lg.logout()

    return df_recon

