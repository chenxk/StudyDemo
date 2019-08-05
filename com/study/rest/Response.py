class Response:
    '''
    返回值定义
    '''
    __message = 'success'
    __code = 0
    __data = {}

    def __init__(self):
        '''
        默认构造方法
        '''

    def __init__(self, code, message):
        '''
        构造方法
        :param code:
        :param message:
        '''
        self.code = code
        self.message = message

    def setData(self, data):
        '''

        :param data:
        :return:
        '''
        self.__data = data

    def getData(self):
        '''

        :return:
        '''
        return self.__data

    def toString(self):
        return
 # def default(self, object):
    #     # return json.JSONEncoder.default(self, object)
    #     if isinstance(object, Response):
    #         return object.__dict__
    #     else:
    #         # call base class implementation which takes care of
    #         # raising exceptions for unsupported types
    #         return json.JSONEncoder.default(self, object)