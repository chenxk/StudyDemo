'''
Python导入模块的方法有两种：import module 和 from module import，区别是前者所有导入的东西使用时需加上模块名的限定，而后者不要。
'''
from com.study.test.cls.Person import Person

p = Person()
'''
这两个效果是一样的
'''
p.prt()
Person.prt(p)

#内置类属性
print(Person.__bases__)
#print(Person.__doc__)
#print(Person.__dict__)
print(Person.__name__)

print(hasattr(p,'age'))
print(hasattr(p,'data'))

p.speak()


print("data:",p.data)
print("data:",Person.data)


print(p._age)
print(Person._age)

#print(Person.__name)

del p


person = Person()
print(person._age)