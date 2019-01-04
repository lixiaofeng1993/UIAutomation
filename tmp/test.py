#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 18:57
# @Author  : lixiaofeng
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import re

data = '已上传8.91MB，共144.82MB'

a = re.findall('(\d+\.\d+)', data)
print(a)