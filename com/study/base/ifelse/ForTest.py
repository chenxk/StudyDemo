import sys

nums = [1, 3, 5]
it = iter(nums)

for i in it:
    print(i)


# it = iter(nums)
# print("-----")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成


for x in f:
    print(x,end=",")

