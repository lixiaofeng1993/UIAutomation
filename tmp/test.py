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

from common.basics import open_browser

d = open_browser()
d.get('https://dev.edu.xxbmm.com')

d.find_element_by_id('username').send_keys('root')
d.find_element_by_id('password').send_keys('admin')
d.find_element_by_xpath('//*[@id="root"]/div[2]/div/form/div[3]/button').click()

