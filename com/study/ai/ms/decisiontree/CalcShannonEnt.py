'''

    计算数据集的香农熵

'''
import operator
from math import log


def calcShannonEnt(dataSet):
    '''
    计算数据集的香农熵

    :param dataSet: 数据集
    :return:
    '''

    # 数据集行数
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        # 最后一个值是标签
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        # 数据集中标签计数
        labelCounts[currentLabel] += 1

    # 香农熵结果
    # 熵越高，混合的数据就越多
    shannonEnt = 0.0
    for key in labelCounts:
        prod = float(labelCounts[key]) / numEntries
        shannonEnt -= prod * log(prod, 2)
    #
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    '''
    划分数据集

    :param dataSet:划分的数据集

    :param axis:划分数据集的特征

    :param value:需要返回的特征的值

    :return:
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
            reducedFeatVec.extend(featVec[axis + 1:])
            # 在列表末尾添加新的对象
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeature(dataSet):
    '''
    选择最好的特征进行分类

    :param dataSet: 分类的数据集

    :return: 特征的索引
    '''

    # 特征数量
    numFeatures = len(dataSet[0]) - 1
    # 数据集的香农熵
    baseEntropy = calcShannonEnt(dataSet)
    # 信息增益
    bestInfoGain = 0.0
    # 特征
    bestFeature = -1
    for i in range(numFeatures):
        # 创建唯一的分类标签列表
        # 取所有行的第i列
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        # 新的熵
        newEntropy = 0.0
        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prod = len(subDataSet) / float(len(dataSet))
            newEntropy += prod * calcShannonEnt(subDataSet)
        # 信息增益
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    '''
    查找最优分类

    :param classList:
    :return:
    '''
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createDataSet():
    dataSet = [[1, 1, 'Y'], [1, 1, 'Y'], [1, 0, 'N'], [0, 1, 'N'], [0, 0, 'N']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# dataSet, labels = createDataSet()
# calcShannonEnt(dataSet)
# print(dataSet)
# print(splitDataSet(dataSet, 1, 0))
# print(splitDataSet(dataSet, 1, 1))
# print(chooseBestFeature(dataSet))

