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
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del trainingSet[randIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print("the error rate is :", float(errorCount / len(testSet)))


spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
spamTest()
