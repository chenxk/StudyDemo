'''
NumPy 数字类型是dtype(数据类型)对象的实例，每个对象具有唯一的特征。 这些类型可以是np.bool_，np.float32等。

https://www.yiibai.com/numpy/numpy_data_types.html

numpy.dtype(object, align, copy)
参数为：

Object：被转换为数据类型的对象。

Align：如果为true，则向字段添加间隔，使其类似 C 的结构体。

Copy? 生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用


字节顺序取决于数据类型的前缀<或>。
<意味着编码是小端(最小有效字节存储在最小地址中)。
>意味着编码是大端(最大有效字节存储在最小地址中)。

'''

import numpy as np

print(np.bool_)

# int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
'''
'b'：布尔值

'i'：符号整数

'u'：无符号整数

'f'：浮点

'c'：复数浮点

'm'：时间间隔

'M'：日期时间

'O'：Python 对象

'S', 'a'：字节串

'U'：Unicode

'V'：原始数据(void)
'''
dt = np.dtype(np.int32)
print(dt)

dt = np.dtype('i4')
print(dt)

dt = np.dtype('>i4')
print(dt)

dt = np.dtype([('age', np.int8)])
print(dt)

dt = np.dtype([('age', np.int8)], align=True)
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print(a['age'])

'''
定义名为 student 的结构化数据类型，其中包含字符串字段name，
整数字段age和浮点字段marks。 此dtype应用于ndarray对象。
'''
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')], align=False)
print(student)
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
'''
Python3的字符串的编码语言用的是unicode编码，由于Python的字符串类型是str，
在内存中以Unicode表示，一个字符对应若干字节，如果要在网络上传输，或保存在磁盘上就需要把str变成以字节为单位的bytes
python对bytes类型的数据用带b前缀的单引号或双引号表示
'ABC'  
b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显得和前者一样，但bytes的每个字符都只占用一个字节
'''
print(a)
