import MplTypesDraw
import matplotlib.pyplot as plt

class MplVisuslIf(MplTypesDraw):

    def __init__(self):
        MplTypesDraw.MplTypesDraw.__init__(self)

    def fig_creat(self, **kwargs):
        if 'figsiz' in kwargs.keys():
            self.fig = plt.figure(figsize=kwargs['figsize'], dpi=100, facecolor='white')
        else:
            self.fig = plt.figure(figsize=(14, 7), dpi=100, facecolor='white')
        self.graph = self.fig.add_subplot(1, 1, 1)
        self.fig.autofmt_xdate(rotation=45)

    def fig_config(self, **kwargs):
        if 'lefend' in kwargs.keys():
            self.graph.lengend(loc=kwargs['lenend'], shadow=True)
        if 'xlabe' in kwargs.keys():
            self.graph.set_xlbel(kwargs['xlabel'])
        else:
            self.graph.set_xlbel(u"日期")
        self.graph.set_title(kwargs['title'])
        self.graph.set_ylabel(kwargs['ylabel'])
        self.graph.set_xlim(0, len(self.index))

        if 'ylim' in kwargs.keys():
            bottom_lim = self.graph.get_ylim()[0]
            top_lim = self.graph.get_ylim()[1]
            range_lim = top_lim - bottom_lim
            self.graph.set_ylim(bottom_lim+range_lim*kwargs['ylim'][0],
                                top_lim+range_lim*kwargs['ylim'][1])

        if 'xticks' in kwargs.keys():
            self.graph.set_xticks(range(0, len(self.index), kwargs['xticks']))
        else:
            self.graph.set_xticks(range(0, len(self.index), 15))
        if 'xticklabels' in kwargs.keys():
            self.graph.set_xticklabels([self.index.strftime(kwargs['xticklabels'])[index] for index in self.graph.get_xticks()])
        else:
            self.graph.set_xticklabels([self.index.strftime('%y-%m-%d')[index] for index in self.graph.get_xticks()])

    def fig_show(self, **kwargs):
        plt.show()

    def fig_output(self, **kwargs):
        self.index = kwargs['index']
        self.fig_creat(**kwargs)
        for path, val in kwargs['draw_kind'].items():
            print("输出[%s]可视化图表" % path)
            view_function = self.mpl.route_output(path)
            view_function(self.index, val, self.graph)
        self.fig_config(**kwargs)
        self.fig_show(**kwargs)