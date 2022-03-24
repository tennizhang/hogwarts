# -*- coding: utf-8 -*-
"""
Name : server.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/15 10:39
Desc :
"""


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api, Namespace
from sqlalchemy import *
from hogwarts.web.log_util import logger
# 实例化flask
app = Flask(__name__)

api = Api(app)
case_ns = Namespace("testcase", description="testcase")
# 进行数据库的配置
# 数据库的用户名
username = "root"
# 数据库的密码
password = "123456"
# 数据库的ip：数据库端口
server = "127.0.0.1:3360"
# 数据库名
dbname = "testcase"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{dbname}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定app
db = SQLAlchemy(app)

# 每个类表示一张表 项目名称、项目编号、项目的描述、项目的状态
class Test(db.Model):
    id = Column(Integer, primary_key=True)
    testcase_name = Column(String(80), nullable=False)
    remarkes = Column(String(800))

@case_ns.route("/")
class TestCase(Resource):
    get_parser = api.parser()
    get_parser.add_argument("testcase_name", type=str, required=True, location="json")
    @case_ns.expect(get_parser)
    def get(self):
        case_id = request.args.get("id")
        if case_id:
            case_data = Test.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            data = [case_data.as_dict()]
            app.logger.info(data)
        else:
            case_data = Test.query.all()
            app.logger.info(case_data)
            data = [i.as_dict() for i in case_data]
            app.logger.info(data)
        return {"error":0, "msg":{'data':data}}

    def delete(self):
        case_id = request.args.get("id")
        if not case_id:
            return {"error":40001, "msg":"delete case_id can't be null"}
        case = TestCase.query.fifter_by(id=case_id).delete()
        app.logger.info(case)
        db.session.commit()
        db.session.close()


if __name__ == '__main__':
    api.add_resource(TestCase, "/testcase")
    app.run(debug=True, port=5000)

