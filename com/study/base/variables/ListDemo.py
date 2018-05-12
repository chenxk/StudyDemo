'''
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：

List是可变的

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表

元组和列表可以互转

'''

lists = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(lists)  # 输出完整列表
print(lists[0])  # 输出列表第一个元素
print(lists[1:3])  # 从第二个开始输出到第三个元素
print(lists[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(lists + tinylist)  # 连接列表

print(lists[::-1])

lists[0] = 100
print(lists)

print("------------")
for x in lists:
    print(x, end="\t")
print()
print("---------")
print(lists.count('runoob'))