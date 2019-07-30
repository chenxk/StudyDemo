'''
这个不是class，这个是纯粹的文件,Python中叫模块

模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

在 Python 中，函数是一等对象。编程语言理论家把“一等对象”定义为满

足下述条件的程序实体：

    在运行时创建

    能赋值给变量或数据结构中的元素

    能作为参数传给函数

    能作为函数的返回结果

'''
import time

'''
format date time
return string
'''


# Python 函数是对象。这里我们创建了一个函数，然后调用它，读取它的 __doc__ 属性，并且确定函数对象本身是 function 类的实例。
def formatDateTime(date=time.localtime(time.time()), formatStr='%Y-%m-%d %H:%M:%S'):
    timeStr = (time.strftime(formatStr, date))
    return timeStr


# Python 函数是对象。这里我们创建了一个函数，然后调用它，读取它的 __doc__ 属性，并且确定函数对象本身是 function 类的实例。
def formatDateTimeBySeconds(dateTime, formatStr='%Y-%m-%d %H:%M:%S'):
    date = time.localtime(dateTime)
    timeStr = (time.strftime(formatStr, date))
    return timeStr


'''
获取当前时间
'''


def getCurrentDateTime():
    return time.localtime(time.time())


'''
获取当前时间戳
'''


def getCurrentTimeMillis():
    return int(time.time() * 1000)


print(formatDateTime(time.localtime(1528584967)))
