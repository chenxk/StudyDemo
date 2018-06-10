import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import csv
import urllib
import matplotlib.dates as mdates
import datetime as dt

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def readFromFile():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    date, closep, highp, lowp, openp, volume = np.loadtxt('example3.txt',
                                                          delimiter=',',
                                                          unpack=True)

    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)

    ax1.plot_date(date, closep, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)

    ax1.fill_between(date, 0, closep)
    '''
    让我们介绍条件填充。 让我们假设图表的起始位置是我们开始买入 eBay 的地方。
     这里，如果价格低于这个价格，我们可以向上填充到原来的价格，然后如果它超过了原始价格，
     我们可以向下填充。 我们可以这样做：
    '''
    #ax1.fill_between(date, closep[0], closep)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0, 25, 50, 75])

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


readFromFile()
