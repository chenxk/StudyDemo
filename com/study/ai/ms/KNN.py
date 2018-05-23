from numpy.ma import array


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [0.2, 0.3]])
    labels = ['A', 'A', 'B', 'B', 'B']
    return group, labels
