import random
import re

from numpy.ma import array

from com.study.ai.ms.bayes.Bayes import *


def textParse(bigString):
    '''
    字符串拆分

    :param bigString:
    :return:
    '''
    tokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in tokens if len(tok) > 2]


def spamTest():
    '''
    邮件测试

    :return:
    '''
    docList = []
    classList = []
    fullTest = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i, encoding='utf-8').read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i, encoding='utf-8').read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    # 总共有50行数据
    trainingSet = list(range(50))
    # 测试数据
    testSet = []
    for i in range(10):
        # 方法将随机生成下一个实数，它在 [x, y) 范围内。
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        # 测试的行号删除
        del trainingSet[randIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    # 通过训练数据，计算贝叶斯分类
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        # 测试分类准不准
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        # 利用训练出来的分类，对数据进行分类，对比分类结果和真实分类
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print("the error rate is :", float(errorCount / len(testSet)))


spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
