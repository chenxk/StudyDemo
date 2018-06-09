import numpy as np

'''
术语广播是指 NumPy 在算术运算期间处理不同形状的数组的能力。 
对数组的算术运算通常在相应的元素上进行。 
如果两个阵列具有完全相同的形状，则这些操作被无缝执行。
'''

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)

a = np.array([1, 2, 3, 4])
b = np.array([[10, 20, 0, 40], [10, 20, 0, 40]])
c = a + b
print(c)

a = np.array([1, 2, 3, 4])
b = np.array([[10, 20, 20, 40], [10, 20, 60, 40]])
c = a / b
print(c)
