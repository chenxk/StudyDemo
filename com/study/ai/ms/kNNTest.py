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
    :return: 返回匹配的标签
    '''
    # 数据集合的行数
    dataSetSize = dataSet.shape[0]
    print(dataSetSize)

    '''
    函数格式tile(A,reps)
　　A和reps都是array_like
　　A的类型众多，几乎所有类型都可以：array, list, tuple, dict, matrix以及基本数据类型int, string, float以及bool类型。
　　reps的类型也很多，可以是tuple，list, dict, array, int, bool.但不可以是float, string, matrix类型。
    '''
    # 行 列
    # Construct an array by repeating A the number of times given by reps.
    # 根据输入向量构建一个二维数组，行数为dataSetSize，列的值为inX
    xDataSet = tile(inX, (dataSetSize, 1))
    print(xDataSet)
    # 矩阵相减,得到输入向量和样本数据差集，用来下一步计算距离
    diffMat = xDataSet - dataSet
    print(diffMat)
    # 取平方
    sqDiffMat = diffMat ** 2  # (p1,p2)^2
    print(sqDiffMat)
    # 矩阵同行中的列相加，得到一维数组
    '''
    （axis=0）表示全部平面上的对应位置，
    （axis=1），每一个平面的每一列，
    （axis=2），每一个平面的每一行。
    '''
    sqDistances = sqDiffMat.sum(axis=1)  # (p1,p2)^2 + (p3,p4)^2 输入向量和样本数据集的距离计算
    print(sqDistances)
    # 数组每个元素开根号
    distances = sqDistances ** 0.5  # 欧式距离计算
    print(distances)  # 得到输入向量和样本集个点的距离
    # argsort函数返回的是数组值从小到大的索引值
    sortedDistIndicies = distances.argsort()
    print(sortedDistIndicies)
    # 定义一个字典
    classCount = {}
    for i in range(k):
        # 命中的标签
        votelLabel = labels[sortedDistIndicies[i]]
        print(votelLabel)
        # 返回指定键的值，如果值不在字典中返回default值
        tempLabel = classCount.get(votelLabel, 0)
        print(tempLabel)
        # 将符合的结果放入字典中，命中计数+1
        classCount[votelLabel] = tempLabel + 1
    # 符合的结果
    print(classCount)
    # 以列表返回可遍历的(键, 值) 元组数组
    # print(classCount.items())
    # operator模块提供的itemgetter函数用于获取对象的哪些维的数据进行排序，参数为一些序号
    # reverse：True 倒叙排序
    print(classCount.items())
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount


# print(classify0(0.2, group, labels, 3))
# print(classify0(2, group, labels, 3))
print(classify0([0.2, 0.5], group, labels, 3))
print(classify0([0.9, 1.5], group, labels, 3))
