# -*- coding: utf-8 -*-
"""
Name : testcase.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 15:51
Desc :
"""
from hogwarts.web.service.testcase import Testcase

"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import request
from flask_restx import Namespace, Resource

from hogwarts.web.log_util import logger
from hogwarts.web.dao.testcase_model import TestCase
from hogwarts.web.live_server import api, db

case_ns = Namespace("case", description="用例管理")

@case_ns.route("")
class TestCaseServer(Resource):
    get_paresr = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_paresr.add_argument("id", type=int, location="args")

    @case_ns.expect(get_paresr)
    def get(self):
        """
        测试用例的查找
        :return:
        """
        # 接口的请求数据信息
        case_id = request.args.get("id")

        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"接收到的参数 <===== {case_id}")
        # 调用service层的具体业务逻辑
        testcase = TestCase()
        datas = testcase.get(case_id)
        return datas

    post_paresr = api.parser()
    post_paresr.add_argument("id", type=int, required=True, location="json")
    post_paresr.add_argument("case_title", type=str, required=True, location="json")
    post_paresr.add_argument("remark", type=str, location="json")

    @case_ns.expect(post_paresr)
    def post(self):
        """
        测试用例的新增
        :return:
        """
        # 获取请求数据
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        case_id = case_data.get("id")
        case_title = case_data.get("case_title")
        remark = case_data.get("remark")
        # case_id
        # 如果不存在，则添加这条记录到库中
        # 如果存在，不执行新增操作， 返回 40001错误码
        testcae = Testcase()
        r = testcae.create(case_id, case_title, remark)
        if r:
            return {"code": 0, "msg": f"case id {case_id} success add."}
        else:
            return {"code": 40001, "msg": "case is exists"}

    put_paresr = api.parser()
    put_paresr.add_argument("id", type=int, required=True, location="json")
    put_paresr.add_argument("case_title", type=str, required=True, location="json")
    put_paresr.add_argument("remark", type=str, location="json")

    @case_ns.expect(put_paresr)
    def put(self):
        """
        测试用例的修改
        :return:
        """
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        case_id = case_data.get("id")
        testcase = Testcase()
        case_data1 = {}
        case_data1["case_title"] = case_data.get("case_title")
        case_data1["remark"] = case_data.get("remark")
        r = testcase.create(case_id, case_data1)
        if r:
            return {"code": 0, "msg": f"case id {case_id} success change to {case_data1}"}
        else:
            return {"code": 40002, "msg": "case is not exists"}

    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, location="json", required=True)

    @case_ns.expect(delete_parser)
    def delete(self):
        """
        测试用例的删除
        :return:
        """
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"接收到的参数id <====={case_id}")
        testcase = Testcase()
        r = testcase.delete(case_id)
        if r:
            return {"code": 0, "msg": f"case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"case is not exists"}
