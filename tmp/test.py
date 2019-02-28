#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 18:57
# @Author  : lixiaofeng
# @Site    : 
# @File    : 1test.py
# @Software: PyCharm
# import random
#
# text = random.uniform(1, 10)
#
# print(round(text, 2))

from jpype import *
import sys

print(get_default_jvm_path())
startJVM(get_default_jvm_path())
java.lang.System.out.println("hello world!")
shutdownJVM()
