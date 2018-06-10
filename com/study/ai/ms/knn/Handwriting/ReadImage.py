import numpy as np

'''
手写识别--读取图片数据
'''

def img2vector(image):
    '''
    每个文件中的数据都是32行32列
    32*32的二进制图形举证转为1*1024的向量

    :param image: 图片名称
    :return:
    '''
    returnVect = np.zeros((1, 1024))
    #print(returnVect)
    fr = open(image, encoding="utf-8")
    # 行
    for i in range(32):
        line = fr.readline()
        # 列
        for j in range(32):
            returnVect[0, 32 * i + j] = int(line[j])
    return returnVect
#print(img2vector('digits/testDigits/0_0.txt')[0, :32])
