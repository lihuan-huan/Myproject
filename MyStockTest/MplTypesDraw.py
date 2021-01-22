from MyStockTest import DefTypesPool
import numpy as np


class MplTypesDraw():
    mpl = DefTypesPool.DeftypePool

    @mpl.route_types(u"line")
    def line_plot(self, df_index, df_dat, graph):
        for key, val in df_dat.items():
            graph.plot(np.arange(0, len(val)), val, label=key, lw=1.0)
