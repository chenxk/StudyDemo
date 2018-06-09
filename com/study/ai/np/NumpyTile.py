import numpy as np

# Construct an array by repeating A the number of times given by reps.
'''
重复提供的数据
tile(A,reps)
A:
(array_like) The input array.
reps:
(array_like) The number of repetitions of A along each axis.

'''
# 3重复4遍
xDataSet = np.tile(3, 4)
print(xDataSet)  # [3 3 3 3]

# 元组重复成二维数组，二维数组为一行，元组在列方向重复三次
xDataSet = np.tile((1, 2), (1, 3))
print(xDataSet)  # [[1 2 1 2 1 2]]

# 集合重复成二维数组，二维数组为二行，数组在列方向重复三次
xDataSet = np.tile([1, 2], (2, 3))
'''
[[1 2 1 2 1 2]]
[[1 2 1 2 1 2]
 [1 2 1 2 1 2]]
 '''
print(xDataSet)

# 集合重复成三维数组，三维数组为二行，三维数组中每一个元素为一个二维数组，
# 二维数组为3行，二维数组的元素是集合在列方向重复两次
xDataSet = np.tile([1, 2], (2, 3, 2))
'''
[ 
  [[1 2 1 2]
  [1 2 1 2]
  [1 2 1 2]]

 [[1 2 1 2]
  [1 2 1 2]
  [1 2 1 2]]
  ]
 '''
print(xDataSet)


print(3**2)
print(3*2)

xDataSet = np.tile((1, 2), (3, 1))
print(xDataSet)
print(xDataSet**2)
sqDistances = xDataSet.sum(axis=1)
print(sqDistances)