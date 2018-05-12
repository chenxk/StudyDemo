from com.study.test.base import DateUtils
from com.study.test.cls.Person import Person

print(DateUtils.getCurrentDateTime().tm_year);

print(Person.__bases__)

for x in range(1, 21):
    print(repr(x).rjust(3), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))



print('hello,{}'.format('tom'))
print('hello,{},your age is {}'.format('tom',22))
print('hello,{},your age is {age}'.format('tom',age = 22))


table = {'Google': 1, 'Runosssob': 2, 'Taobao': 3}

for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))


import  math
print("PI:{0:.5f}".format(math.pi))
print("PI:{0:.5f}".format(1/3))

print("p %3.2f" % math.pi)


table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))


str = input('enter')
print('input:{0}'.format(str))

print("说的水电费")