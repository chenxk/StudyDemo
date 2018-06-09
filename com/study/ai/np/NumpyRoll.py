import numpy as np

a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 将轴 2 滚动到轴 0(宽度到深度)

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2))
'''
arr：输入数组
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置。
'''
# 将轴 0 滚动到轴 1：(宽度到高度)
print('\n')

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2, 1))

print("轴的理解")
X = np.random.randint(0, 5, [3, 2, 2])
print(X)
'''
如果将三维数组的每一个二维看做一个平面（plane，X[0, :, :], X[1, :, :], X[2, :, :]），
三维数组即是这些二维平面层叠（stacked）出来的结果。
则
（axis=0）表示全部平面上的对应位置，
（axis=1），每一个平面的每一列，
（axis=2），每一个平面的每一行。
'''
print("axis=0", X.sum(axis=0))
print("axis=1", X.sum(axis=1))
print("axis=2", X.sum(axis=2))
