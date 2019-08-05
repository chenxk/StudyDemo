from com.study.rest.Response import Response

per = Response(200, 'sss')
per.setData("good")
# print(per.__data)
print(per.getData())
