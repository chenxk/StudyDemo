from numpy.ma import array

from com.study.ai.ms.bayes.Bayes import *

postingList, classVec = loadDataSet()
print(postingList)
print(classVec)

myVocabList = createVocabList(postingList)
print(myVocabList)

setOfWords = setOfWords2Vec(myVocabList, postingList[0])
print(setOfWords)
setOfWords = setOfWords2Vec(myVocabList, ['mr', 'mt', 'abc', 'hh'])
print(setOfWords)

trainMatrix = []
for doc in postingList:
    # 每行文档的单词在全文本中命中的结果
    trainMatrix.append(setOfWords2Vec(myVocabList, doc))

p0Vect, p1Vect, pAbusive = trainNB0(array(trainMatrix), array(classVec))
print(p0Vect)
print(p1Vect)
print(pAbusive)

testEntry = ['love', 'my', 'dalmation']
thisDoc = setOfWords2Vec(myVocabList, testEntry)
print(classifyNB(thisDoc, p0Vect, p1Vect, pAbusive))

testEntry = ['love', 'garbage', 'stupid']
thisDoc = setOfWords2Vec(myVocabList, testEntry)
print(classifyNB(thisDoc, p0Vect, p1Vect, pAbusive))
