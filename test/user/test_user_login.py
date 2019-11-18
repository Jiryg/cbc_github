# @author : 'CBC'
# @Time   : 2019-11-14
# @File   : test_user_login


import unittest
import requests
import json
from lib.read_excel import *


class TestUserLogin(unittest.TestCase):   # 类必须Test开头，继承TestCase才能识别为用例类
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        print(os.getcwd())
        cls.data_list = excel_to_list("data/test_user_data.xlsx", "TestUserLogin")  # 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    url = 'http://115.28.108.130:5000/api/user/login/'

    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        # data = {"name": "张三", "password": "123456"}
        # res = requests.post(url=self.url, data=data)
        # print(res.text)
        # self.assertIn("登录成功", res.text)  # 断言
        case_data = get_test_data(self.data_list, 'test_user_login_normal')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        print("期望的结果是：" + expect_res)

        res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
        print("实际的结果是：" + res.text)
        self.assertEqual(res.text, expect_res)  # 改为assertEqual断言

    def test_user_login_wrong_password(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        print(res.text)
        self.assertIn("失败", res.text)


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别