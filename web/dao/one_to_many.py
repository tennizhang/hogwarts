# -*- coding: utf-8 -*-
"""
Name : one_to_many.py
Author : Tenni Zhang
Contect : 470145262@qq.com
Time : 2022/3/20 17:38
Desc :
"""
from hogwarts.web.server import db
from sqlalchemy import *

# Project 为1 ， Plan为多
class ProjectModel(db.Model):
    __tablename__ = "project"
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    name = db.Column(String(80), nullable=False, unique=True)

class PlanModel(db.Model):
    __tablename__ = "plan"
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    name = db.Column(String(80), nullable=False, unique=True)
    # 通过外键设置一对多表的关联关系
    project_id = Column(Integer, ForeignKey("project.id"))
    # 第一个参数，表示这个关系的另一端是ProjectModel类也就是"1"，
    # 第二个参数backref，表示反向引用，需要从1反向获取多的时候使用的属性
    projects = db.relationship("ProjectModel", backref="plans")

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    ## ====一对多===数据的添加
    # project1 = ProjectModel(id=1, name="微信项目")
    # project2 = ProjectModel(id=2, name="飞书项目")
    # 外键的参数为，多对一状态下，多要关联那个1
    # plan1 = PlanModel(id=1, name="成员管理", project_id=1)
    # plan2 =  PlanModel(id=2, name="部门管理", project_id=1)
    # db.session.add_all([plan1, plan2])
    # db.session.commit()
    # db.session.close()
    ## ====一对多===数据的查询
    # 由多查一， 获取 plan1 对应的项目名称
    # plan1 = PlanModel.query.filter_by(id=1).first()
    # print(plan1.projects.name)
    # 由一查多
    # project1 = ProjectModel.query.filter_by(id=1).first()
    # plans 的属性名一定要与 backref="plans" 的一致
    # print(project1.plans[0].name)
    ## ====一对多===
    # 由一改多数据的修改
    # project1 = ProjectModel.query.filter_by(id=1).first()
    # project1.plans[0].name = "成员管理2"
    # db.session.commit()
    # db.session.close()
    # 由多改1
    # plan1 = PlanModel.query.filter_by(id=1).first()
    # plan1.projects.name = "微信项目2"
    # db.session.commit()
    # db.session.close()
    ##======删除======
    # 删除微信项目对应的计划， 其实删除没有很便捷的方式，本质就是通过条件进行删除
    # project1 = ProjectModel.query.filter_by(id=1).first()
    # PlanModel.query.filter(PlanModel.project_id == project1.id).delete()
    # db.session.commit()
    # db.session.close()
    print(PlanModel.query.all())