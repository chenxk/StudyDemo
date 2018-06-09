import numpy as np

'''
NumPy 包包含一个迭代器对象numpy.nditer。 它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。 
数组的每个元素可使用 Python 的标准Iterator接口来访问。
'''

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('修改后的数组是：')
for x in np.nditer(a):
    print(x, end=' ')

# 迭代的顺序匹配数组的内容布局，而不考虑特定的排序。 这可以通过迭代上述数组的转置来看到。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
b = a.T
print('原始数组的转置是：')
print(b)
print('\n')
print('修改后的数组是：')
for x in np.nditer(b):
    print(x, end=' ')

# 如果相同元素使用 F 风格顺序存储，则迭代器选择以更有效的方式对数组进行迭代。
# C(按行)、F(按列)或A(任意，默认)。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
b = a.T
print('原始数组的转置是：')
print(b)
print('\n')
print('以 C(按行) 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, )
print('\n')
print('以 F(按列) 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=' ')

print('op_flags...')

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    # x[...] = 2 * x
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

print("按行输出")
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=' ')

print()
print("广播迭代")
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
for x, y in np.nditer([a, b]):
    print('%d:%d' % (x, y), end=' ')
