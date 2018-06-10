import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import array

from com.study.ai.ms.knn import KNNData

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def show1():
    labels = 'frogs', 'hogs', 'dogs', 'logs'
    sizes = 15, 20, 45, 10
    colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
    explode = 0, 0.1, 0, 0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


def show2():
    mat, labels = KNNData.file2matrix('data.txt')
    print(mat)
    print(mat[:, 1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 输出数组的第二列和第三列
    ax.scatter(mat[:, 1], mat[:, 2], 10 * array(labels), 10 * array(labels))
    plt.show()


def show3():
    mat, labels = KNNData.file2matrix('data.txt')
    norMat, ranges, minVals = KNNData.autoNorm(mat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print(labels)
    # scatter（X，Y，S,C）S确定每个标记的面积。 S可以是与X和Y相同长度的矢量或标量。如果S为空，
    # C确定每个标记的颜色。
    ax.scatter(norMat[:, 1], norMat[:, 2], 25 * array(labels), 15 * array(labels))
    plt.xlabel('吃鸡')
    plt.ylabel('吃冰激凌')
    plt.title('Interesting Graph\nCheck it out')

    plt.legend([(0, 'zaza'), (15, 'nor'), (30, 'good'), (45, 'vg')])
    # plt.legend(['zaza','nor','good','vg'])

    plt.show()


def findData(mat, labels):
    '''
    将数据按照标签进行分组

    :param mat:
    :param labels:
    :return:
    '''
    labelMap = {}
    for x in range(labels.__len__()):
        label = labels[x]
        data = labelMap.get(label, np.empty([0,3]))
        ls = []
        ls.append(mat[x])
        #print(np.array(ls))
        data = np.append(data, np.array(list(ls)), axis=0)
        labelMap[label] = data
    return labelMap


def show4():
    mat, labels = KNNData.file2matrix('data.txt')
    norMat, ranges, minVals = KNNData.autoNorm(mat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #print(labels)
    # ax.scatter(norMat[:, 1], norMat[:, 2], 25 * array(labels), 15 * array(labels))

    dataMap = findData(mat=norMat, labels=labels)
    # print(mat)
    # print(dataMap[0])
    # print(mat[:, 1])
    # print(dataMap[0][:, 1])

    p0 = plt.scatter(dataMap[0][:, 1], dataMap[0][:, 2], marker='x', color='m', label='渣渣', s=30)

    p1 = plt.scatter(dataMap[1][:, 1], dataMap[1][:, 2], marker='+', color='r', label='屌丝', s=30)

    p2 = plt.scatter(dataMap[2][:, 1], dataMap[2][:, 2], marker='o', color='g', label='普通', s=30)

    p3 = plt.scatter(dataMap[3][:, 1], dataMap[3][:, 2], marker='*', color='b', label='好人', s=30)

    # scatter（X，Y，S,C）S确定每个标记的面积。 S可以是与X和Y相同长度的矢量或标量。如果S为空，
    # C确定每个标记的颜色。
    # ax.scatter(norMat[:, 1], norMat[:, 2], 25 * array(labels), 15 * array(labels))
    plt.xlabel('吃鸡')
    plt.ylabel('吃冰激凌')
    plt.title('Interesting Graph\nCheck it out')

    # plt.legend([(0, 'zaza'), (15, 'nor'), (30, 'good'), (45, 'vg')])
    # plt.legend(['zaza','nor','good','vg'])
    plt.legend(loc='upper right')

    plt.show()


# show1()
# show2()
# show3()
show4()



# mat, labels = KNN.file2matrix('data2.txt')
# dataMap = findData(mat=mat, labels=labels)
# print(dataMap)
# print(dataMap[1])
# print(dataMap[1][:,1])
