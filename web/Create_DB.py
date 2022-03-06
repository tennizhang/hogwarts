
# 导入 flask 和 flask_sqlalchemy
from unittest import TestCase

import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api, Namespace
from sqlalchemy import *
from hogwarts.web.log_util import logger
# 实例化flask
app = Flask(__name__)

api = Api(app)
case_ns = Namespace("case", description="project")
# 进行数据库的配置
# 数据库的用户名
username = "root"
# 数据库的密码
password = "123456"
# 数据库的ip：数据库端口
server = "127.0.0.1:3360"
# 数据库名
dbname = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{dbname}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定app
db = SQLAlchemy(app)

# 每个类表示一张表 项目名称、项目编号、项目的描述、项目的状态
class Project(db.Model):
    id = Column(Integer, primary_key=True)
    project_name = Column(String(80), nullable=False)
    project_number = Column(String(20), unique=False)
    project_description = Column(String(80))
    project_status = Column(String(20))

@case_ns.route("/")
class TestProject(Resource):
    get_parser = api.parser()
    get_parser.add_argument("project_name", type=str, required=True, location="json")
    get_parser.add_argument("project_number", type=str, required=True, location="json")
    @case_ns.expect(get_parser)
    def get(self):
        case_id = request.args.get("id")
        if case_id
            case_data = Project.query.filter_by(id=case_id).first()
            if case_data:
                datas = [{"id":case_data.id,"project_name"case_data.project_name,"project_number"case_data.project_number,
                        "project_description"case_data.project_description,"project_status"case_data.project_status}]
            else:
                datas = []
        else:
            case_datas = Project.query.all()
            datas = [ {"id":case_data.id,"project_name"case_data.project_name,"project_number"case_data.project_number,
                        "project_description"case_data.project_description,"project_status"case_data.project_status}
                            for case_data in case_datas]
        return datas

    post_parser = api.parser()
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("project_name", type=str, required=True, location="json")
    post_parser.add_argument("project_number", type=str, required=True, location="json")
    post_parser.add_argument("project_description", type=str, location="json")
    post_parser.add_argument("project_status", type=str, location="json")
    @case_ns.expect(post_parser)
    def post(self):
        # 请求数据
        case_data = request.json
        logger.info(f"got data=====  {case_data}")
        case_id = case_data.get(id)
        # 查询数据库是否有记录
        exists = Project.query.filter_by(id=case_id).first()
        if not exists:
            testcase = Project(**case_data)
            db.session.add(testcase)
            db.session.commit()
            return {"code": 0, "msg": "data added"}
        else:
            return {"code": 40001, "msg": "data exists"}

    put_parser = api.parser()
    put_parser.add_argument("project_name", type=str, required=True, location="json")
    put_parser.add_argument("project_number", type=str, required=True, location="json")
    @case_ns.expect(put_parser)
    def put(self)
        case_data = request.json
        logger.info(f"got data=====  {case_data}")
        case_id = case_data.get(id)
        exists = Project.query.filter_by(id=case_id).first()
        if not exists:
            return {"code":40002, "msg":"data not exist"}
        else:
            case_data["project_name"] = case_data.get("project_name")
            case_data["project_number"] = case_data.get("project_number")
            case_data["project_description"] = case_data.get("project_description")
            case_data["project_status"] = case_data.get("project_status")
            Project.query.filter_by(id=case_id).update(case_data)
            db.session.commit()
            return {"code":0, "msg":f"{case_id} update success"}

    delete_parser = api.parser()
    delete_parser.add_argument("project_name", type=str, required=True, location="json")
    delete_parser.add_argument("project_number", type=str, required=True, location="json")
    @case_ns.expect(delete_parser)
    def delete(self):
        case_data = request.json
        logger.info(f"got data=====  {case_data}")
        case_id = case_data.get(id)
        exists = Project.query.filter_by(id=case_id).first()

        if exists:
            Project.query.filter_by(id=case_id).delete()
            db.session.commit()
            return {"code":0, "msg":"case deleted"}
        else:
            return {"code":40002, "msg":"case not exist"}

api.add_namespace(case_ns, "/testcase")

if __name__ == '__main__':
    app.run(debug=True)
    # 创建表
    #db.create_all()
    # 删除表
    #db.drop_all()
    '''
    project1 = Project(project_name='abc', project_number='acbc0001', project_description='this is a project', project_status='unable')
    db.session.add_all([project1])
    db.session.commit()
    db.session.close()
    '''