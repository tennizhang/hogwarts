# -*- coding: utf-8 -*-
"""
Name : testcase_model.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 15:50
Desc :
"""
# dao 层，只负责和数据库交互相关，供上层service调用。
from sqlalchemy import *

from hogwarts.web.live_server import db
from hogwarts.web.log_util import logger


class TestCase(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    case_title = db.Column(String(80), nullable=False, unique=True)
    # 备注
    remark = db.Column(String(120))


    @classmethod
    def get_all(cls):
        return  cls.query.all()

    @classmethod
    def get_by_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, case_id, case_title, remark):
        testcase = cls(id=case_id, case_title=case_title, remark=remark)
        logger.info(f"将要存储的内容为<======{testcase}")
        db.session.add(testcase)
        db.session.commit()
        db.session.close()

    @classmethod
    def delete(cls, **kwargs):
        cls.query.filter_by(**kwargs).delete()
        # commit 之后需要添加close
        db.session.commit()
        db.session.close()

    @classmethod
    def update(cls, case_id, case_data1):
        cls.query.filter_by(id=case_id).update(case_data1)
        db.session.commit()
        db.session.close()