import math

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=",")
        a, b = b, a + b


fibonacci(20)

print()


def prt(str):
    '''
    xxxxxxyyy
    \n
    :param str: xxxx
    \n
    :return:
    '''
    print(str)


prt("yyyyy")
prt(str="xxx")


def add(a, b):
    '''
    简单的加法运算\n
    :param a: 第一个值
    :param b: 第二个值
    :return: 运算结果
    '''
    return a + b


print(add(1, 3))

'''

@:param a
@:param b
@:param c
'''
def reduce(a, b, c:'参数的注释可以这样写，NB啊'):
    return a + b + c


print(reduce(a=1, b=3, c=4))


'''
不定长参数
'''
def mulitParam(name,*info):
    print(name)
    for x in info:
        print(x)



mulitParam("xxx",2,4,5)

print("lambda....")
sum = lambda item, x : item + x

print(sum(3,4))


'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
'''
x = int(2.9)  # 内建作用域
print(x)
g_count = 0  # 全局作用域
print("old g_count",g_count)

def outer():
    g_count = 10
    print("new g_count",g_count)
    o_count = 1  # 闭包函数外的函数中
    print("old o_count", o_count)
    def inner():
        i_count = 2  # 局部作用域
        o_count = 9
        print("new o_count", o_count)
    inner()
    print("old o_count", o_count)

outer()
print("old g_count",g_count)



'''
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问，如下代码：
'''

if True:
    msg = 'good'
print(msg)

'''
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''

sum = 23
def getSum():
    global sum
    print(sum)
    sum = 10


getSum()
print(sum)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)

outer()


a = 10
def test():
    global a
    a = a + 1
    print(a)
test()