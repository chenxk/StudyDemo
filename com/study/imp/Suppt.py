def su():
    print('su san say')


def _test():
    print("xxxx")

def __test2():
    print("2xx")


def run():
    print("run")

def add():
    print("add method....")

'''

说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。

'''

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir())
# print('__name__:',__name__)
# print('__doc__:',__doc__)
# print('__file__:',__file__)
# print('__loader__:',__loader__)
# print('__package__:',__package__)
# print('__spec__:',__spec__)
# print('__annotations__:',__annotations__)
# print('__builtins__:',__builtins__)
# print('__cached__:',__cached__)