# -*- coding:utf-8  -*-
import chardet
import codecs



file = codecs.open('E:\\test.sql','a+','utf-8')



i = 0
for line in file:
    i += 1
    print('line num:{},content:{}'.format(i,line))


#file = codecs.open('E:\\test.sql','r','utf-8')
file.write('\nAAAA');

file.close();