import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import csv
import urllib
import matplotlib.dates as mdates
import datetime as dt

from com.study.test.base import DateUtils

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

'''
matplotlib.pyplot是一些命令行风格函数的集合，使matplotlib以类似于MATLAB的方式工作。
每个pyplot函数对一幅图片(figure)做一些改动：比如创建新图片，在图片创建一个新的作图区域(plotting area)，
在一个作图区域内画直线，给图添加标签(label)等。
matplotlib.pyplot是有状态的，亦即它会保存当前图片和作图区域的状态，新的作图函数会作用在当前图片的状态基础之上。
'''


def readFromFile():
    x = []
    y = []

    with open('example.txt', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

    plt.plot(x, y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def readFromFileByNp():
    x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
    plt.plot(x, y, label='Loaded from file!')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def readFromNetword(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'
    print(stock_price_url)
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y%m%d')})

    plt.plot_date(date, closep, '-', label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def dateFormat(val):
    saleDate = int(val)/1000
    year = DateUtils.formatDateTimeBySeconds(saleDate, '%Y')
    print(year)
    return year


def readFromFile2():
    date, closep, highp, lowp, openp, volume = np.loadtxt('example2.txt',
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: dateFormat})

    plt.plot_date(date, closep, '-', label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()



def readFromFile3():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    date, closep, highp, lowp, openp, volume = np.loadtxt('example3.txt',
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y%m%d')})

    ax1.plot_date(date, closep, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()




def readFromFile4():
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

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()



# readFromFile()
# readFromFileByNp()
# readFromNetword('TSLA')
# readFromFile2()
# readFromFile3()
readFromFile4()