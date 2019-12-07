# -*- coding: UTF-8 -*-
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


def formatNumber(number):
    '''
    number 必须是带区号的
    '''

    code = 0
    message = 'success'
    data = {'number': number, 'isValid': None}

    print "number:", number
    x = phonenumbers.parse(number, None)
    print x
    data['countryCode'] = x.country_code
    data['nationalNumber'] = x.national_number
    # a = phonenumbers.is_possible_number(x)
    # 验证是否是可用的
    b = phonenumbers.is_valid_number(x)
    print b
    data['isValid'] = b
    # 格式化
    rx = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print rx
    data['format'] = rx
    # 地区
    c = geocoder.description_for_number(x, "en")
    print c
    data['region'] = c
    #运营商
    d = carrier.name_for_number(x, "en")
    print(d)
    data['carrier'] = d

    print data
    #phonenumbers.is_possible_number_string()


formatNumber("+8615678475646")
formatNumber("+442083661177")

number = "+" + "ss"
print number
