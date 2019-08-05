# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from validate_email import validate_email
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


class DoEmail(Resource):
    def get(self, email):
        code = 0
        message = 'success'
        data = {'email': email, 'isValid': None}
        try:
            logger.info('valid email:{0}'.format(email))
            is_valid = validate_email(email, verify=True)
            data = {'email': email, 'isValid': is_valid}
        except Exception as err:
            logger.error(err, exc_info=True)
            code = 1000
            message = 'valid fail'
        # return json.JSONEncoder.default(result)
        return {'code': code, 'message': message, 'data': data}


api.add_resource(DoEmail, '/check/<email>')

# if __name__ == '__main__':
#    app.run(debug=True, port=8100)

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('0.0.0.0', 8100, app)
logger.info("Serving HTTP on port 8100...")
# 开始监听HTTP请求:
httpd.serve_forever()