'''
这个不是class，这个是纯粹的文件

在 Python 中，函数是一等对象。编程语言理论家把“一等对象”定义为满

足下述条件的程序实体：

    在运行时创建

    能赋值给变量或数据结构中的元素

    能作为参数传给函数

    能作为函数的返回结果

'''
import  time


'''
format date time
return string
'''
#Python 函数是对象。这里我们创建了一个函数，然后调用它，读取它的 __doc__ 属性，并且确定函数对象本身是 function 类的实例。
def formatDateTime(date = time.localtime(time.time()),formatStr = '%Y-%m-%d %H:%M:%S'):
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
    return int(time.time()*1000);

