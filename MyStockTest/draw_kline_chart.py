import MplVisuakIf
import bs_k_data_stock
app = MplVisuakIf.MplVisuslIf
def draw_kline_chart(stock_dat):
    layout_dict = {'figsize':(12, 6)
                   , 'index': stock_dat.index
                   , 'draw': {'ochl':
                                {'open': stock_dat.Open
                               , 'close': stock_dat.Close
                               , 'High': stock_dat.High
                               , 'Low':stock_dat.Low
                                }
                         }
                    , 'title': u"000651"
                    , 'ylabel': u"价格"
                   }
    app.fig_ouy(**layout_dict)

df = bs_k_data_stock.bs_k_data_stock("sz.000651", '2020-01-01', '2020-01-20')
draw_kline_chart(df.copy(deep=True))