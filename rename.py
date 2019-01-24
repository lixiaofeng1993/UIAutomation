#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 11:40
# @Author  : lixiaofeng
# @Site    : 
# @File    : rename.py
# @Software: PyCharm

import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'case')
py_path_list = os.listdir(path)
for i in py_path_list:
    py_path = os.path.join(path, i)
    if 'child' in i:
        os.rename(py_path, os.path.join(path, '1' + os.path.basename(py_path)))
