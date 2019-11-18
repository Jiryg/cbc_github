# @author : 'CBC'
# @Time   : 2019-11-16
# @File   : logger

import logging
import os


def logger():
    # prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # log_file = os.path.join(prj_path, 'log', 'log.txt')
    logging.basicConfig(level=logging.DEBUG,  # log levelformat='[%(asctime)s] %(levelname)s
                        # [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                        datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                        # filename=log_file,  # 日志输出文件
                        # filemode='a'  # 追加模式
                        )