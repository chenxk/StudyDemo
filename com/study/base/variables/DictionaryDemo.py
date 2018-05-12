'''
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
'''

dicts = {}
dicts['one'] = "1 - 菜鸟教程"
dicts[2] = "2 - 菜鸟工具"

print(dicts)

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dicts['one'])  # 输出键为 'one' 的值
print(dicts[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print(tinydict['site'])
# key不存在会报错
# print(tinydict['xxx'])

dicts = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dicts)

dicts = {x: x ** 2 for x in (2, 4, 6)}
print(dicts)

dicts = dict(Runoob=1, Google=2, Taobao=3)
print(dicts)

#16进制
print(hex(23))

