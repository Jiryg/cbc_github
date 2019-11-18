# @author : 'CBC'
# @Time   : 2019-11-14
# @File   : run_all

import unittest
from config.config import *
from lib.HTMLTestReportCN import HTMLTestRunner


logging.info("================================== 测试开始 ==================================")

suite = unittest.defaultTestLoader.discover(test_path)


with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

# send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")