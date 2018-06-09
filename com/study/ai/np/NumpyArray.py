import numpy as np

'''
NumPy 中定义的最重要的对象是称为 ndarray 的 N 维数组类型。 
它描述相同类型的元素集合。 可以使用基于零的索引访问集合中的项目。

ndarray中的每个元素在内存中使用相同大小的块。 ndarray中的每个元素是数据类型对象的对象(称为 dtype)。

基本的ndarray是使用 NumPy 中的数组函数创建的，如下所示：
numpy.array
它从任何暴露数组接口的对象，或从返回数组的任何方法创建一个ndarray。

'''
a = np.array([1, 2, 3])
'''
1.	object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
2.	dtype 数组的所需数据类型，可选。
3.	copy 可选，默认为true，对象是否被复制。
4.	order C(按行)、F(按列)或A(任意，默认)。
5.	subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
6.	ndimin 指定返回数组的最小维数
'''
print(a)

# 创建一个dtype对象persontype，通过其字典参数描述结构类型的各个字段。
persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})
'''
S32 : 32个字节的字符串类型，由于结构中的每个元素的大小必须固定，因此需要指定字符串的长度
i : 32bit的整数类型，相当于np.int32
f : 32bit的单精度浮点数类型，相当于np.float32
'''
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)],
             dtype=persontype)
'''
然后我们调用array函数创建数组，通过关键字参数 dtype=persontype， 
指定所创建的数组的元素类型为结构persontype。
运行上面程序之后，我们可以在IPython中执行如下的语句查看数组a的元素类型
'''
print('dtype:', a.dtype)
'''
这里我们看到了另外一种描述结构类型的方法： 一个包含多个组元的列表，其中形如 (字段名, 类型描述) 
的组元描述了结构中的每个字段。类型描述前面为我们添加了 '|', '<' 等字符，这些字符用来描述字段值的字节顺序：
| : 忽视字节顺序
< : 低位字节在前
> : 高位字节在前

[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')]

'''

print(a)
print(a[0])
print(a[0]['name'])
print(a[:]['name'])

a = np.array([[1, 2], [3, 4]])
print(a)

# 最小维度
a = np.array([[1, 2, 3], [4, 5]], ndmin=3)
print(a)

# complex 复数
a = np.array([1, 2, 3], dtype=complex)
print(a)

print("-----------------------")
# 数组元素为0，因为它们未初始化。
x = np.empty([3, 2], dtype=int)
print(x)

# 含有 5 个 0 的数组，默认类型为 float
x = np.zeros(5)
print(x)

x = np.zeros((2, 2), dtype=np.int)
print(x)

print("-----")
x = np.zeros((2, 2, 3), dtype=np.int)
print(x)

x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x)

'''
numpy.ones
返回特定大小，以 1 填充的新数组。
'''
x = np.ones(5)
print(x)

x = np.ones((3, 3), dtype=float)
print(x)

x = [1, 2, 3]
a = np.asarray(x)
print(a)

x = (1, 2, 3)
a = np.asarray(x)
print(a)

x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)

'''
numpy.frombuffer
此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回ndarray。
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
'''

# s = "Hello World"
# a = np.frombuffer(s)
# print(a)

list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)
