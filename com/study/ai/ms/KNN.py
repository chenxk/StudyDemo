from numpy import tile
from numpy.ma import array, zeros, shape


def createDataSet():
    '''
    准备数据

    :return:
    '''
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [0.5, 0.6]])
    labels = ['A', 'A', 'B', 'B', 'C']
    return group, labels


def file2matrix(file):
    '''
    从文件中读取数据

    :param file: 文件名称
    :return:
    '''
    fr = open(file)
    lines = fr.readlines()
    numberOfLines = len(lines)
    # 初始化数组  numberOfLines 行，3 列
    returnMat = zeros((numberOfLines, 3))
    # print(returnMat)
    classLabelVector = []
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split(' ')
        # print(type(listFromLine))
        # print(len(listFromLine))
        # print((listFromLine))
        # 将读到的数据写入数组中
        returnMat[index, :] = listFromLine[0:3]
        # 将最后一个数据当做标签
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    '''
    归一化数值

    :param dataSet: 集合
    :return:
    '''
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    # 获取dataset的维度
    normDataSet = zeros(shape(dataSet))
    # 集合的行数
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
