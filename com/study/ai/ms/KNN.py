from numpy.ma import array, zeros


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [0.2, 0.3]])
    labels = ['A', 'A', 'B', 'B', 'B']
    return group, labels


def file2matrix(file):
    '''
    从文件中读取数据
    :param file:
    :return:
    '''
    fr = open(file)
    lines = fr.readlines()
    numberOfLines = len(lines)
    returnMat = zeros((numberOfLines, 3))
    #print(returnMat)
    classLabelVector = []
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split(' ')
        #print(type(listFromLine))
        #print(len(listFromLine))
        #print((listFromLine))
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

