# -*- coding: UTF-8 -*-
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number_x = '+8617767170190'
#number_x = '+8618621017090'
number_y = '2784402772'
number_z = '02083661177'

# （1）电话号码解析
x = phonenumbers.parse(number_x, None)
y = phonenumbers.parse(number_y, 'CN')
z = phonenumbers.parse(number_z, 'GB')


rx = phonenumbers.format_number(x,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print rx

print(x)
print(y)
print(z)

# （2）电话号码检测
a = phonenumbers.is_possible_number(x)
b = phonenumbers.is_valid_number(x)

print('is_possible_number:', a)
print('is_valid_number:', b)

# （3）基于解析的电话号码（区域）联系人 信息挖掘

c = geocoder.description_for_number(x, "en")
print(c)
print "000000"
ro_number = phonenumbers.parse(number_x, "CN")
d = carrier.name_for_number(x, "CN")
print(d)
print('000000\n')

# （4）基于文本内容的电话号码挖掘
text = "Call me at 15208214953 if it's before 9:30, or on 13557766882 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "CN"):
    d = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
    print(d)



def formatNumber(number):
    x = phonenumbers.parse(number, None)