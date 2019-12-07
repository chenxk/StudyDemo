# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from validate_email import validate_email
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
import logging
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

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
            logger.info('valid result:{0}'.format(data))
        except Exception as err:
            logger.error(err, exc_info=True)
            code = 1000
            message = 'valid fail'
        # return json.JSONEncoder.default(result)
        return {'code': code, 'message': message, 'data': data}


class DoNumber(Resource):
    def get(self, number):
        code = 0
        message = 'success'
        data = {'number': number, 'isValid': None}

        try:
            if not number.startswith("+"):
                number = "+" + number
            logger.info('valid number:{0}'.format(number))
            x = phonenumbers.parse(number, None)
            data['countryCode'] = x.country_code
            data['nationalNumber'] = x.national_number
            # a = phonenumbers.is_possible_number(x)
            # 验证是否是可用的
            b = phonenumbers.is_valid_number(x)
            data['isValid'] = b
            # 本国格式化
            rx = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
            data['nationalFormat'] = rx
            # 国际格式化
            rx = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            data['internationalFormat'] = rx
            # 地区
            c = geocoder.description_for_number(x, "en")
            data['region'] = c
            # 运营商
            d = carrier.name_for_number(x, "en")
            data['carrier'] = d
            logger.info('valid result:{0}'.format(data))
        except Exception as err:
            logger.error(err, exc_info=True)
            code = 1000
            message = 'valid fail'
        return {'code': code, 'message': message, 'data': data}


api.add_resource(DoEmail, '/check/email/<email>')
api.add_resource(DoNumber, '/check/number/<number>')

# if __name__ == '__main__':
#    app.run(debug=True, port=8100)

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('0.0.0.0', 8100, app)
logger.info("Serving HTTP on port 8100...")
# 开始监听HTTP请求:
httpd.serve_forever()
