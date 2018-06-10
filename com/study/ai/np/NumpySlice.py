import numpy as np

'''

ndarray对象中的元素遵循基于零的索引。 有三种可用的索引方法类型： 字段访问，基本切片和高级索引。

基本切片是 Python 中基本切片概念到 n 维的扩展。 
通过将start，stop和step参数提供给内置的slice函数来构造一个 Python slice对象。 
此slice对象被传递给数组来提取数组的一部分。
'''

a = np.arange(10)
s = slice(2, 7, 1)
print(a)
print(a[s])

# 通过将由冒号分隔的切片参数(start:stop:step)直接提供给ndarray对象，也可以获得相同的结果。
print(a[2:7:1])
print(a[2:7:])

print(a[3])
print(a[3:])

'''
切片还可以包括省略号(...)，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的ndarray。
'''
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6], [7, 8, 0]])
print('我们的数组是：')
print(a)
print('\n')
# 这会返回第二列元素的数组：
print('第二列的元素是：')
print(a[..., 1])
print('\n')
# 现在我们从第二行切片所有元素：
print('第二行的元素是：')
print(a[1, ...])
print('第一行之后的元素是：')
print(a[1:, ...])
print('\n')
# 现在我们从第二列向后切片所有元素：
print('第二列及其剩余元素是：')
print(a[..., 1:])

'''
高级索引

以下示例获取了ndarray对象中每一行指定列的一个元素。 因此，行索引包含所有行号，列索引指定要选择的元素
'''
x = np.array([[1, 2], [3, 4], [5, 6]])
# 需要取得数据分别为 (行，列):(0,0) = 1 ，（1,1） = 4，（2,0） = 5
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
print(rows)
cols = np.array([[0, 2], [0, 2]])
print(cols)
y = x[rows, cols]
# 需要取得数据分别为 (行，列):左上角(0,0) = 0 ，右上角（0,2） = 2，左下角（3,0） = 9 ，右下角 （3,2） = 11
print('这个数组的每个角处的元素是：')
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
# 切片
z = x[1:4, 1:3]
print('切片之后，我们的数组变为：')
print(z)
print('\n')
# 对列使用高级索引
y = x[1:4, [1, 2]]
print('对列使用高级索引来切片：')
print(y)

# 当结果对象是布尔运算(例如比较运算符)的结果时，将使用此类型的高级索引。
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
# 现在我们会打印出大于 5 的元素
print('大于 5 的元素是：')
print(x[x > 5])
print(x[x > 5])

# 这个例子使用了~(取补运算符)来过滤NaN
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a[np.iscomplex(a)])
