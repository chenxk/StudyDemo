import pymysql
from validate_email import validate_email
from com.study.test.base import DateUtils

# 打开数据库连接
db = pymysql.connect("localhost", "chen", "chen", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

sql = "SELECT * FROM T_EMAIL "
cursor.execute(sql)
data = cursor.fetchall()
updateSql = "update T_EMAIL set valid_res = '{0}' where id = {1}"
for row in data:
    # print(row)
    id = row[0]
    email = row[1]
    res = row[3]
    if res == None:
        try:
            print("begin valid email: ", email, " ,", DateUtils.formatDateTime())
            time = DateUtils.getCurrentTimeMillis()
            is_valid = validate_email(email, verify=True)
            print("end ", DateUtils.formatDateTime(), "cost time:", (DateUtils.getCurrentTimeMillis() - time))
            sql = updateSql.format(is_valid, id)
            print(sql)
            cursor.execute(sql)
            # break
        except Exception as err:
            print(err)
# print(data)
db.commit()

# 关闭数据库连接
db.close()
