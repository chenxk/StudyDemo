from numpy import tile

import operator

from com.study.ai.ms import KNN

group, labels = KNN.createDataSet()
print(group)
print(labels)


def classify0(inX, dataSet, labels, k):
    '''
    kNN算法
    :param inX: 输入向量
    :param dataSet: 训练集
    :param labels: 标签向量
    :param k: 最近邻居个数
    :return:
    '''
    dataSetSize = dataSet.shape[0]
    print(dataSetSize)

    '''
    函数格式tile(A,reps)
　　A和reps都是array_like
　　A的类型众多，几乎所有类型都可以：array, list, tuple, dict, matrix以及基本数据类型int, string, float以及bool类型。
　　reps的类型也很多，可以是tuple，list, dict, array, int, bool.但不可以是float, string, matrix类型。
    '''
    # 行 列
    xDataSet = tile(inX, (dataSetSize, 1))
    print(xDataSet)
    # 矩阵相减
    diffMat = xDataSet - dataSet
    print(diffMat)
    # 取平方
    sqDiffMat = diffMat ** 2
    print(sqDiffMat)
    # 矩阵同行相加，得到一维数组
    sqDistances = sqDiffMat.sum(axis=1)
    print(sqDistances)
    # 数组每个元素开根号
    distances = sqDistances ** 0.5
    print(distances)
    # argsort函数返回的是数组值从小到大的索引值
    sortedDistIndicies = distances.argsort()
    print(sortedDistIndicies)
    # 定义一个字典
    classCount = {}
    for i in range(k):
        votelLabel = labels[sortedDistIndicies[i]]
        print(votelLabel)
        # 返回指定键的值，如果值不在字典中返回default值
        tempLabel = classCount.get(votelLabel, 0)
        print(tempLabel)
        # 将符合的结果放入字典中
        classCount[votelLabel] = tempLabel + 1
    # 符合的结果
    print(classCount)
    # 以列表返回可遍历的(键, 值) 元组数组
    # print(classCount.items())
    # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]


print(classify0(0.2, group, labels, 3))
print(classify0(2, group, labels, 3))
print(classify0([0.2, 0.5], group, labels, 3))
print(classify0([0.9, 1.5], group, labels, 3))
