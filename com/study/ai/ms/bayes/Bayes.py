from numpy.ma import zeros, ones, log


def loadDataSet():
    '''
    创建数据集

    :return:
    '''
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    '''
    得到集合中所有去重后的单词

    :param dataSet:数据集合

    :return: 去重后的单词数组
    '''
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def bagOfWords2Vec(vocabList, inputSet):
    '''
    词袋模型

    将输入向量和vocabList进行比较，如果inputSet的单词和vocabList有命中,标记出来

    :param vocabList: 不重复的单词列表

    :param inputSet: 输入单词列表

    :return: 输入单词列表命中的结果
    '''

    # 初始化一个向量
    returnVet = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVet[vocabList.index(word)] += 1
        else:
            print("the word:%s is not in my vocalulary!" % word)
    return returnVet


def setOfWords2Vec(vocabList, inputSet):
    '''
    词集模型

    将输入向量和vocabList进行比较，如果inputSet的单词和vocabList有命中,标记出来

    :param vocabList: 不重复的单词列表

    :param inputSet: 输入单词列表

    :return: 输入单词列表命中的结果
    '''

    # 初始化一个向量
    returnVet = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVet[vocabList.index(word)] = 1
        else:
            print("the word:%s is not in my vocalulary!" % word)
    return returnVet


def trainNB0(trainMatrix, trainCategroy):
    '''
    朴素贝叶斯分类器,计算正面负面词汇概率

    :param trainMatrix: 文档矩阵

    :param trainCategroy: 文档分类向量

    :return:正面词汇占比，负面词汇占比，负面文档占比
    '''
    # 文档矩阵的行数
    numTrainDocs = len(trainMatrix)
    # 每行的单词个数  每行单词量一样
    numWords = len(trainMatrix[0])
    # 负面文档占比
    pAbusive = sum(trainCategroy) / float(numTrainDocs)
    # 正面词汇矩阵
    p0Num = ones(numWords)
    # 负面词汇矩阵
    p1Num = ones(numWords)

    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        # 每行文档的分类
        if trainCategroy[i] == 1:
            # 负面文档向量+1
            p1Num += trainMatrix[i]
            # 负面单词总数累加
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 正面词汇占比
    p0Vect = log(p0Num / p0Denom)
    # 负面词汇占比
    p1Vect = log(p1Num / p1Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass):
    '''
    朴素贝叶斯分类函数

    :param vec2Classify: setOfWords2Vec 处理后的文档向量

    :param p0Vec:正面概率

    :param p1Vec:负面概率

    :param pClass:负面文档概率

    :return: 0：正面 1：负面
    '''
    p1 = sum(vec2Classify * p1Vec) + log(pClass)
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass)
    if p1 > p0:
        return 1  # 负面
    else:
        return 0  # 正面
