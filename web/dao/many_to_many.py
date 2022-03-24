# -*- coding: utf-8 -*-
"""
Name : many_to_many.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 18:05
Desc :
"""
# 中间表， 第一个参数是中间表表名
# 第二个，第三个参数分别对应主键
from sqlalchemy import *

from hogwarts.web.server import db

testcase_plan_rel = db.Table('testcase_plan_rel',
                    db.Column('testcase_id', db.Integer,
                              db.ForeignKey('testcase.id'),
                              primary_key=True),
                    db.Column('plan_id', db.Integer,
                              db.ForeignKey('plan.id'),
                              primary_key=True))

class TestCaseModel(db.Model):
    __tablename__ = "testcase"
    id = db.Column(db.Integer, primary_key=True)
    case_title = db.Column(db.String(80), nullable=False, unique=True)
    remark = db.Column(db.String(120))


class PlanModel(db.Model):
    __tablename__ = "plan"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    # 这一句是设置多对多的关键地方
    # 第一个参数'TestCaseModel'，表示这个关系的另一端是TestCaseModel类
    # 第二个参数secondary指向了中间表，中间表只包含关系的两侧表的主键列
    # 第三个参数backref，表示反向引用
    testcases = db.relationship("TestCaseModel",
                                secondary=testcase_plan_rel,
                                backref=db.backref('plans'))