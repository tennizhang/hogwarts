# -*- coding: utf-8 -*-
"""
Name : live_server.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 15:53
Desc :
"""

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


# 数据库的用户名
username = "root"
# 数据库的密码
password = "123456"
# 数据库的ip：数据库端口
server = "127.0.0.1:3360"
# 数据库名
db = "testcase"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)
# 导包
def get_router():
    from router.testcase import case_ns
    api.add_namespace(case_ns, "/testcase")


if __name__ == '__main__':
    get_router()
    app.run(debug=True, port=5000)
