#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 18:02
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_yun.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.basics import open_browser, Crazy
import os, time

# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Ie(executable_path='D:\\UIAutomation\driver\IEDriverServer.exe')
action = ActionChains(driver)
# driver = webdriver.Chrome(executable_path='D:\\UIAutomation\driver\chromedriver.exe')
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
time.sleep(3)
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
# time.sleep(3)
# 使用组合键ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# time.sleep(3)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'b')
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.LEFT_ALT, 'a')
action.send_keys(Keys.ALT, 'a').perform()
# action.send_keys('x').perform()
# driver.find_element_by_id("kw").send_keys(Keys.ALT, 'x')
time.sleep(3)