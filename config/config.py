import logging
import os
import time

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下

# now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
# report_name = now + '.html'
report_name = 'index.html'
report_file = os.path.join(prj_path, 'report', report_name)  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='w')  # a追加模式, w清空再写入模式

# if run_all.type == '-l':
    # 本地数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'test'
db_passwd = '123456abc'
db = 'api_test'
# elif run_all.type == '-r':
#     # 远程数据库配置
#     db_host = '115.28.108.130'
#     db_port = 3306
#     db_user = 'test'
#     db_passwd = '123456'
#     db = 'api_test'
# else:
#     print("参数错误")


# 邮件配置
# smtp_server = 'smtp.sina.com'
# smtp_user = 'test_results@sina.com'
# smtp_password = 'hanzhichao123'
#
# sender = smtp_user  # 发件人
# receiver = '2375247815@qq.com'  # 收件人
# subject = '接口测试报告'  # 邮件主题
