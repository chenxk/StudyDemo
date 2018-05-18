import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "chen", "chen", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

sql = "SELECT * FROM t_user_openid "
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
    print(row)
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])

#print(data)

# 关闭数据库连接
db.close()