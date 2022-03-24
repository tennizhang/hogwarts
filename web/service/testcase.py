# -*- coding: utf-8 -*-
"""
Name : testcase.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 15:51
Desc :
"""
# 服务层
from hogwarts.web.dao.testcase_model import TestCase
from hogwarts.web.log_util import logger
from hogwarts.web.server import db


class Testcase:
    def get(self, case_id=None):
        if case_id:
            # 如果不为空，查询操作
            case_data = TestCase.get_by_filter(id=case_id)
            logger.info(f"{case_data}")
            if case_data:
                datas = [{"id": case_data.id,
                          "case_title": case_data.case_title,
                          "remark": case_data.remark}]
                logger.info(f"要返回的数据为<======{datas}")
            else:
                datas = []
        else:
            # 为空，返回所有记录
            case_datas = TestCase.get_all()
            datas = [{"id": case_data.id,
                      "case_title": case_data.case_title,
                      "remark": case_data.remark} for case_data in case_datas]
        return datas

    def create(self,  case_id, case_title, remark):
        case_id = case_id
        # 查询数据库，查看是否有记录
        # exists = TestCase.query.filter_by(id=case_id).first()
        exists = TestCase.get_by_filter(id=case_id)
        logger.info(f"查询表结果：{exists}")
        if not exists:
            TestCase.create( case_id, case_title, remark)
            return True
        else:
            return False

    def delete(self, case_id):
        exists = TestCase.get_by_filter(id=case_id)
        if exists:
            TestCase.delete(id=case_id)
            return True
        else:
            return False

    def update(self, case_id, case_data1):
        # 查询数据库，查看是否有记录
        exists = TestCase.get_by_filter(id=case_id)
        logger.info(f"查询表结果：{exists}")
        # 如果不存在，则 不执行修改操作 并返回 40002
        # 如果存在，执行修改操作
        if exists:

            TestCase.update(case_id, case_data1)
            return True
        else:
            return False