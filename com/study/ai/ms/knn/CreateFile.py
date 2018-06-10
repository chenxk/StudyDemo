import codecs
import random

'''
|r|仅读，待打开的文件必须存在|  
|w|仅写，若文件已存在，内容将先被清空|  
|a|仅写，若文件已存在，内容不会清空|  
|r+|读写，待打开的文件必须存在|  
|w+|读写，若文件已存在，内容将先被清空|  
|a+|读写，若文件已存在，内容不会清空|  
|rb|仅读，二进制，待打开的文件必须存在|  
|wb|仅写，二进制，若文件已存在，内容将先被清空|  
|ab|仅写，二进制，若文件已存在，内容不会清空|  
|r+b|读写，二进制，待打开的文件必须存在|  
|w+b|读写，二进制，若文件已存在，内容将先被清空|  
|a+b|读写，二进制，若文件已存在，内容不会清空|
'''
file = codecs.open('data.txt', 'w', 'utf-8')
lines = 100
for i in range(lines):
    fly = i * 100 * random.randint(1, 10)  # 飞行里程
    game = i * random.randint(3, 15)
    ice = random.randint(1, 20)
    other = random.randint(6, 25)
    lab = random.randint(0, 3)
    file.write('%d %d %d %d %d' % (fly, game, ice, other, lab))
    print(i)
    if (i < lines - 1):
        file.write('\n')
file.close()
