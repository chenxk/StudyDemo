import sys

from com.study.imp import Suppt
from com.study.imp.Suppt import *
#from com.study.imp.Suppt import _test, __test2


'''

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入
语法:import module1[, module2[,... moduleN]

Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
语法:from modname import name1[, name2[, ... nameN]]


一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？

这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。

这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。

搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量，做一个简单的实验，在交互式解释器中，输入以下代码：


'''

print('syspath:',sys.path)


su()

run()

add()


#_test()
#__test2()

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir(Suppt))



