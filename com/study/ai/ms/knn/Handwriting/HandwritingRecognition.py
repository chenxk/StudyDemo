from os import listdir

from com.study.ai.ms.knn.Handwriting.ReadImage import *
from com.study.ai.ms.knn.kNN import classify0

'''
手写识别test
'''


def handwritingTest():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % (fileNameStr))

    testFileList = listdir('digits/testDigits')
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % (fileNameStr))
        classResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with:%d, the real answer is : %d" % (classResult[0][0], classNumStr))
        if classResult[0][0] != classNumStr:
            errorCount += 1
    print("the total error rate is :%f ,errorCount:%d, numTest:%d" % (errorCount / float(mTest), errorCount, mTest))



def handwritingTestSimple():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % (fileNameStr))

    testFileList = listdir('digits/studyDigits')
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % (fileNameStr))
        classResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with:%d, the real answer is : %d" % (classResult[0][0], classNumStr))
        if classResult[0][0] != classNumStr:
            errorCount += 1
    print("the total error rate is :%f ,errorCount:%d, numTest:%d" % (errorCount / float(mTest), errorCount, mTest))


# handwritingTest()
handwritingTestSimple()
