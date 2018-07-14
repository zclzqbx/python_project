#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: zhuchuanlin
# Created Time : Mon 18 Jun 2018 05:53:59 AM PDT
# File Name: file_oper.py
# Description:
"""



import os
import os.path

path = "/home/walker/Documents/py_prj/"


for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in  dirnames:                       #输出文件夹信息
         print("parent is:%s"%(parent))
         print("dirname is:%s"%(dirname))

    for filename in filenames:                        #输出文件信息
         print("parent is:%s"%(parent))
         print("filename is:%s"%(filename))
         print("the full name of the file is:%s"%(os.path.join(parent,filename))) #输出文件路径信息
