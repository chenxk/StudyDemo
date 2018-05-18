class Person:
    '''

    以下划线开头的标识符是有特殊意义的。
    没有下划线开头 foo 的代表公共变量，类似java中的public；
    以单下划线开头 _foo 的代表不能直接访问的类属性，类似java中的protected，需通过类提供的接口进行访问，不能用 from xxx imp * 而导入；
    以双下划线开头的 __foo 代表类的私有成员，类似java中的private；
    以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

    '''

    #可以直接访问，通过类的实例或者类自身
    #类变量，它的值将在这个类的所有实例之间共享
    data = [2,4,5]
    #私有变量,无法从外部访问
    __name = 'xxxx'
    #不能直接访问的类属性
    _age = 23
    def speak(self):
        data = [2.2]
        print(data)

    #类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
    def __init__(self):
        print("构造方法执行")
    #公共方法
    def prt(self):
        print(self)
        print(self.__class__)

    #私有方法
    def __privateMethod(self):
        print('private method exec...')

    #析构函数(destructor) 与构造函数相反，当对象结束其生命周期时（例如对象所在的函数已调用完毕），系统自动执行析构函数。析构函数往往用来做“清理善后” 的工作
    def __del__(self):
        self.__privateMethod()
        class_name = self.__class__.__name__
        print(class_name,'销毁')