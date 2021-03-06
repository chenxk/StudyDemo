import math
import random
#Number
'''
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
'''

age = 80
print("age:",age)
print(isinstance(age,int))
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
print(type(age))

# 取整，得到一个整数
# // 得到的不一定是整数类型的数，它跟分母分子的数据类型有。
print(5 // 4)
print(5 // 4.0)
# 除法，得到一个小数
print(5 / 4)
# 取余
print(17 % 3 )

print(abs(-9))
print(math.exp(2))
print(math.ceil(2.6))
print(math.ceil(2.16))

print(range(10))
print(random.choice(range(10)))

#随机数来一个
print(int(random.random()*100))