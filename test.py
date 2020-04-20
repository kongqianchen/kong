# -*- coding: utf-8 -*-
from flask import Flask
import pymysql

app = Flask(__name__)
# 连接mysql字符串
db = pymysql.connect("localhost", "root", "123456", "k")
# 新建游标
cursor = db.cursor()
# 执行sql语句
#cursor.execute("select * from person")
cursor.execute("select * from person where id = '2'")
data = cursor.fetchone()
print str(data).decode("string_escape")
@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)