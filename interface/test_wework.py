import uuid

import jsonpath
import requests


class TestWeworkCase:

    def setup_class(self):
        """
        获取 access_token 的第二种方法
        """
        # 定义凭证
        corpid = "wwbff14b5ebe798c7b"
        corpsecret = "IGpaqSHi9uHnd5-dpPvr0Vw-0D295fBO5ZUe24Fz7C0"

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发 get 请求
        r = requests.get(url, params=params)
        # 打印响应
        print(r.json())

        access_token = r.json()['access_token']
        self.access_token = access_token

    def test_create_department(self):
        # 拼接url  使用类的实例变量 self.access_token 拼接 access_token 必输字段
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}"
        # # 发送数据体的构造
        # id = 10
        # data = {
        #     "name": "广州研发中心",
        #     "name_en": "RDGZ",
        #     "parentid": 1,
        #     "order": id,
        #     "id": id
        # }
        # # 发起post请求 使用 json=xxx 这样操作  requests 会将我们的字典通过json字符串发送给服务端
        # # res = requests.post(url, json=data)
        # res = requests.request(method="post", url=url, json=data)
        # 打印返回信息
        # 部门名称增加 uuid 进行排重
        _id = str(uuid.uuid4()).split("-")[0]
        res = self.create_department(_id)
        # 断言接口请求成功
        # 调用查询接口获取查询到的数据
        search_rs = self.search_department()
        # 通过jsonpath 获取所有的部门id
        ids = jsonpath.jsonpath(search_rs, "$..id")
        assert res in ids

    def search_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}"
        res = requests.request(method="get", url=url)
        return res.json()

    def create_department(self, _id):
        # 拼接url  使用类的实例变量 self.access_token 拼接 access_token 必输字段
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}"
        # 发送数据体的构造
        data = {
            "name": f"广州研发中心_{_id}",
            "name_en": f"RDGZ_{_id}",
            "parentid": 1,
        }
        # 发起post请求 使用 json=xxx 这样操作  requests 会将我们的字典通过json字符串发送给服务端
        # res = requests.post(url, json=data)
        res = requests.request(method="post", url=url, json=data)
        print(res.json())
        return res.json()["id"]

    def test_update_department(self):
        # 调用创建部门操作
        _id = str(uuid.uuid4()).split("-")[0]
        department_id = self.create_department(_id)
        # 拼接url  使用类的实例变量 self.access_token 拼接 access_token 必输字段
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}"
        # 发送数据体的构造
        data = {
            "id": department_id,
            "name": f"广州研发中心_更新_{department_id}",
            "name_en": f"RDGZ_UPDATE_{department_id}",
            "parentid": 1,
        }
        # 发起post请求 使用 json=xxx 这样操作  requests 会将我们的字典通过json字符串发送给服务端
        # res = requests.post(url, json=data)
        res = requests.request(method="post", url=url, json=data)
        # 打印返回信息
        print(res.json())
        # 断言接口请求成功
        assert res.json()["errcode"] == 0