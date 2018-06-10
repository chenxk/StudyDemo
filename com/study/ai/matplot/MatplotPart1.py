import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

'''
matplotlib.pyplot是一些命令行风格函数的集合，使matplotlib以类似于MATLAB的方式工作。
每个pyplot函数对一幅图片(figure)做一些改动：比如创建新图片，在图片创建一个新的作图区域(plotting area)，
在一个作图区域内画直线，给图添加标签(label)等。
matplotlib.pyplot是有状态的，亦即它会保存当前图片和作图区域的状态，新的作图函数会作用在当前图片的状态基础之上。
'''


def line1():
    '''
    一元一次方程

    :return:
    '''
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y, '')
    plt.show()


def sin():
    # 计算正弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sine wave form")
    # 使用 matplotlib 来绘制点
    plt.plot(x, y)
    plt.show()


def sincos():
    # 计算正弦和余弦曲线上的点的 x 和 y 坐标
    x = np.arange(0, 5 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # 建立 subplot 网格，高为 2，宽为 1
    # 激活第一个 subplot
    plt.subplot(2, 1, 1)
    # 绘制第一个图像
    plt.plot(x, y_sin)
    plt.title('Sine')
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    # 展示图像
    plt.show()


def bar():
    '''
    柱状图

    :return:
    '''
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, label='第一组', align='center')
    plt.bar(x2, y2, label='第二组', color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.legend()
    plt.show()


def doubleLine():
    '''
    双线图

    :return:
    '''
    x = [1, 2, 3]
    y = [5, 7, 4]

    x2 = [1, 2, 3]
    y2 = [10, 14, 12]
    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')

    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()  # 显示plot方法中定义的label
    plt.show()


def hist():
    '''
    直方图

    倾向于通过将区段组合在一起来显示分布。 这个例子可能是年龄的分组，或测试的分数。
    我们并不是显示每一组的年龄，而是按照 20 ~ 25，25 ~ 30... 等等来显示年龄。


    :return:
    '''
    population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
                       110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
                       65, 54, 44, 43, 42, 48]

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

    plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='年龄分布')

    plt.xlabel('年龄段')
    plt.ylabel('个数')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def scatter():
    '''
    散点图

    :return:
    '''
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x, y, label='skitscat', color='k', s=25, marker="o")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def stackplot():
    '''
    堆叠图

    :return:
    '''
    days = [1, 2, 3, 4, 5]
    sleeping = [7, 8, 6, 11, 7]
    eating = [2, 3, 4, 3, 2]
    working = [7, 8, 7, 2, 2]
    playing = [8, 5, 7, 8, 13]

    plt.plot([], [], color='m', label='Sleeping', linewidth=5)
    plt.plot([], [], color='c', label='Eating', linewidth=5)
    plt.plot([], [], color='r', label='Working', linewidth=5)
    plt.plot([], [], color='k', label='Playing', linewidth=5)

    plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

    plt.xlabel('日期-天')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def pie():
    '''
    饼状图

    :return:
    '''
    slices = [7, 2, 2, 13]
    activities = ['sleeping', 'eating', 'working', 'playing']
    cols = ['c', 'm', 'r', 'b']
    plt.pie(slices,
            labels=activities,
            colors=cols,
            #我们可以选择指定图形的『起始角度』。
            # 这使你可以在任何地方开始绘图。 在我们的例子中，我们为饼图选择了 90 度角，
            # 这意味着第一个部分是一个竖直线条。
            startangle=90,
            shadow=True,
            #我们总共有四个切片，所以对于explode，如果我们不想拉出任何切片，
            # 我们传入0,0,0,0。 如果我们想要拉出第一个切片，我们传入0.1,0,0,0。
            explode=(0, 0.1, 0, 0),
            autopct='%1.1f%%')
    plt.title('Interesting Graph\nCheck it out')
    plt.show()


# line1()
# sin()
# sincos()
# bar()
# doubleLine()
# hist()
# scatter()
# stackplot()
pie()
