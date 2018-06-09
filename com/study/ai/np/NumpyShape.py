import numpy as np

a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a)
'''
ndarray.shape
这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
'''
print(a.shape)  # (2,3)
print(np.shape(a))  # (2,3)
print(a.shape[0])
print(a.shape[1])

a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)
a.shape = (1, 6)
print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])
# NumPy 也提供了reshape函数来调整数组大小。
b = a.reshape(3, 2)
print(b)

# ndarray.ndim 这一数组属性返回数组的维数。
a = np.arange(24, dtype=np.float)
print(a)
b = a.reshape(3, 2, 2, 2)
print(b)
print(b.ndim)

print(b[2])
# 该函数返回数组上的一维迭代器，行为类似 Python 内建的迭代器。
print(a.flat[2])

'''
numpy.ndarray.flatten
该函数返回折叠为一维的数组副本，函数接受下列参数：
'''
print(b.flatten())
# order：'C' — 按行，'F' — 按列，'A' — 原顺序，'k' — 元素在内存中的出现顺序。
print(b.flatten(order='F'))

# 这一数组属性返回数组中每个元素的字节单位长度。
print(b.itemsize)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(x.itemsize)
'''
ndarray对象拥有以下属性。flags这个函数返回了它们的当前值。

1.	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
2.	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
3.	OWNDATA (O) 数组的内存从其它对象处借用
4.	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
5.	ALIGNED (A) 数据和任何元素会为硬件适当对齐
6.	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新
WRITEBACKIFCOPY : False
'''
print(x.flags)
