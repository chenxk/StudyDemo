# 默认为读取模式
readFile = open('D:\logs\dataimport.log')
# 一次性读取完成
content = readFile.read()
print(content)


readFile = open('D:\logs\dataimport.log')
print("read line.....")
line = readFile.readline()
print(line)

readFile = open('D:\logs\dataimport.log')
print("read lines.....")
line = readFile.readlines()
i = 0
for l in line:
    i += 1
    print('line num:', i, end=" ")
    print(l)

#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
print(readFile.tell())

readFile = open('D:\logs\dataimport.log','a')
print("write lines.....")
readFile.write("xxxxxxxxx")

readFile.close()


value = ('www.runoob.com', 14)
s = str(value)
print(s)