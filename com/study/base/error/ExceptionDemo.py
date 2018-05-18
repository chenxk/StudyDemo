while True:
    try:
        x = int(input("Please enter a number: "))
        print('input number:', x)
        break
    except ValueError as err:
        print(err)
        print("Oops!  That was no valid number.  Try again   ")

import sys

try:
    f = open('D:\logs\新建文本文档.txt', encoding="utf-8")
    s = f.readline()
    print(s)
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
    # 抛出异常
    raise
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
