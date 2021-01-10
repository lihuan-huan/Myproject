import baostock as bs
import pandas as pd
#                                                每笔交易数量  差价设定
def main(stock, start_date, end_date, res, cnt, deal_cnt , threshold):
    print(str(stock)+ " " + str(start_date)  + " " + str(end_date) + " " + str(res) + " " + str(cnt)  + " " + str(deal_cnt) +" " +
          str(threshold) )
    lg = bs.login(user_id="anonymous", password="123456")
    fields = "date,open,high,low" #,close,volume"

    df_bs = bs.query_history_k_data(stock, fields, start_date=start_date, end_date=end_date
                                        ,frequency="d",adjustflag="2")
    data_list = []
    # ['2019-12-02', '3.4409873800', '3.4599983600', '3.4409873800', '3.4409873800', '120396297']
    while (df_bs.error_code == '0') & df_bs.next():
            data_list.append(df_bs.get_row_data())
   #      252965.48217999988 7000 303 346
    #     1156879.0882330008 7000 303 346  sh.601288
    #     2401466.933288 7000 974 1017
    #res = 100000.0
    #cnt = 50000
    jin = 0
    print(data_list[1:10])
    chu = 0
    del_cnt = 0
    success = 0
    print()
    for i in data_list:
        del_cnt += 1
        open = float(i[1])
        high = float(i[2])
        low = float(i[3])
        ii = 1
        jj = 1

        if(open + threshold <= high and cnt >= deal_cnt): # and res > (open + threshold) * deal_cnt ):
            chu += 1
            ii = 0
            cnt -= deal_cnt
            res += (open + threshold) * deal_cnt
        if(open - threshold >= low and res >= (open - threshold) * deal_cnt ):
            jin += 1
            jj = 0
            cnt += deal_cnt
            res -= (open - threshold) * deal_cnt

        if(ii == 1 and jj == 1): success += 1
    print(str(res) + " " + str(cnt) + " " + str(del_cnt) + " " + str(jin) + " " + str(chu) + " " + str(success))

    # result = pd.DataFrame(data_list,columns=df_bs.fields)
    # result.close = result.close.astype('float64')
    # result.open = result.open.astype('float64')
    # result.low = result.low.astype('float64')
    # result.high = result.high.astype('float64')
    # result.volume = result.volume.astype('int')
    # result.index = pd.to_datetime(result.date)
    #
    # print(result.tail())
    # print(result.axes)
    # #print(result.info)

    bs.logout('anonymous')

if __name__ == "__main__":
    main("sh.601288", "2018-05-01", "2021-01-01",123456789.0,1000,1000,0.01)