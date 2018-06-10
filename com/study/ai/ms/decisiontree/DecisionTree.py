'''
决策树

'''
from com.study.ai.ms.decisiontree.CalcShannonEnt import *


def createTree(dataSet, labels):
    '''
    决策树构建

    :param dataSet: 数据集

    :param labels: 特征

    :return:
    '''
    # 最后一列是分类
    classList = [example[-1] for example in dataSet]
    # 类别完全相同停止划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 遍历完所有特征时返回出现次数最多的分类
    # dataSet的元素为 [1, 1, 'Y']，前两个1代表特征，最后一个是分类
    if len(dataSet[0]) == 1:  # 最后一个值是分类，表示特征遍历完成
        return majorityCnt(classList)
    # 当前数据集最好的特征索引
    bestFeat = chooseBestFeature(dataSet)
    # 对应的分类标签
    bestFeatLabel = labels[bestFeat]
    # myTree的value还是个map
    myTree = {bestFeatLabel: {}}
    del labels[bestFeat]
    # 最好的特征索引，得到一组特征列表
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    # 不同的特征再次进行拆分
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


dataSet, labels = createDataSet()
print(createTree(dataSet, labels))
