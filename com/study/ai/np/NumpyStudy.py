import numpy
from numpy import tile

randMat = numpy.random.rand(4,4)
print(randMat)

#在列方向上重复[0,0] 2次，行1次
# res : [2 2]
val = numpy.tile(2, 2)
print(val)

#在列方向上重复[0,0] 3次，行1次
# res : [1 2 3 1 2 3 1 2 3]
print(tile((1, 2, 3), 3))

a = [[1, 2, 3], [5, 4]]
#在列方向上重复[0,0]2次，行1次
# res : [list([1, 2, 3]) list([5, 4]) list([1, 2, 3]) list([5, 4])]
# 列 ，行默认为1
print(tile(a, 2))
print()

#
a = [[1, 2, 3], [5, 4]]
#在列方向上重复[0,0]3次，行2次
'''
[
    [list([1, 2, 3]) list([5, 4]) list([1, 2, 3]) list([5, 4]) list([1, 2, 3]) list([5, 4])] 
    [list([1, 2, 3]) list([5, 4]) list([1, 2, 3]) list([5, 4]) list([1, 2, 3]) list([5, 4])]
]
'''
# [行，列]
print(tile(a, [2, 3]))
# [行，列]
print(tile(a, (2, 3)))
