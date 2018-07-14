#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: zhuchuanlin
# Created Time : Sat 16 Jun 2018 07:31:16 AM PDT
# File Name: logex.py
# Description:
"""


import logging
import os
import sys
import logging.handlers

class Log:
    def __init__(self, module='defautl_module', level=logging.DEBUG, path='/home/walker/Log/'):
         # 创建一个logger
        self.logger = logging.getLogger(module)
        self.logger.setLevel(level)

        err_log_path = os.path.join(path, "Error_Log")

        shell_order = "mkdir -p %s"%(err_log_path)
        if os.system(shell_order) != 0:
            print("Create dir failed:%s!"%(shell_order))
            return

        #Run log handler
        is_dir_exist = os.path.exists(path)
        if not is_dir_exist:
            print("%s is not exist!"%(path))
            return

        filename = path + ("%s.log"%(module))
        # 创建一个handler，用于写入日志文件
        fh = logging.handlers.RotatingFileHandler(filename, maxBytes=10*1024*1024, backupCount=10)
        fh.setLevel(logging.DEBUG)

        #error log handler
        is_dir_exist = os.path.exists(err_log_path)
        if not is_dir_exist:
            print("%s is not exist!"%(err_log_path))
            return

        filename = err_log_path + ("/%s_err.log"%(module))
        #Create error log hander
        fh_err = logging.handlers.RotatingFileHandler(filename, maxBytes=10*1024*1024, backupCount=10)
        fh_err.setLevel(logging.ERROR)

         # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)s %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        fh_err.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh_err)


        #rename
        self.write_log_fatal = self.logger.fatal
        self.write_log_error = self.logger.error
        self.write_log_warning = self.logger.warning
        self.write_log_info = self.logger.info
        self.write_log_debug = self.logger.debug


if __name__ == '__main__':
    logger = Log()
    logger.write_log_fatal("live or death")
    logger.write_log_warning("try to live long")
