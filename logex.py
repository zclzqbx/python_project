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

class Log:
    def __init__(self, module='defautl_module', path='/home/walker/Log/', level=logging.DEBUG):
         # 创建一个logger
        self.logger = logging.getLogger(module)
        self.logger.setLevel(level)

        is_dir_exist = os.path.exists(path)
        if not is_dir_exist:
            os.makedirs(path, 777)

        filename = path + ("%s.log"%(module))

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)

         # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)s %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


        self.write_log_fatal = self.logger.fatal
        self.write_log_error = self.logger.error
        self.write_log_warning = self.logger.warning
        self.write_log_info = self.logger.info
        self.write_log_debug = self.logger.debug


if __name__ == '__main__':
    logger = Log()
    logger.write_log_fatal("live or death")
