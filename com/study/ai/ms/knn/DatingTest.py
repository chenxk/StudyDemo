from com.study.ai.ms.kNNTest import classify0

from com.study.ai.ms.knn import KNNData


def datingClassTest():
    '''
    测试

    :return:
    '''

    mat, labels = KNNData.file2matrix('data.txt')
    hoRatio = 0.1
    norMat, ranges, minVals = KNNData.autoNorm(mat)
    # 总行数
    m = norMat.shape[0]
    # 测试行数
    numTest = int(m * hoRatio)
    errorCount = 0
    for i in range(numTest):
        classResult = classify0(norMat[i, :], norMat[numTest:m, :], labels[numTest:m], 3)
        print("the classifier came back with:%d, the real answer is : %d" % (classResult[0][0], labels[i]))
        if classResult[0][0] != labels[i]:
            errorCount += 1
    print("the total error rate is :%f ,errorCount:%d, numTest:%d" % (errorCount / float(numTest), errorCount, numTest))


datingClassTest()