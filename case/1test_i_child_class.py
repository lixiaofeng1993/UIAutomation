#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 10:35
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_h_child_cla.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from selenium.common.exceptions import *
from BeautifulReport import BeautifulReport
from page.page_child_class import ChildClassPage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class Testcla(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.cla = ChildClassPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_cla')
    def test_a_cla(self):
        """进入分类管理"""
        cla = self.cla
        cla.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        cla.click_cla_manage()
        cla.elements_all_manage()[1].click()
        self.assertEqual(cla.text_check_cla_text(), '分类管理', '进入分类管理栏失败！')
        self.log.info('进入 分类管理 成功.')
        self.save_img('分类管理')

    @BeautifulReport.add_test_img('test_b_new_add_cla')
    def test_b_new_add_cla(self):
        """新增测试分类"""
        cla = self.cla
        self.assertEqual(cla.text_check_cla_text(), '分类管理', '当前页面不在标签管理栏，无法进行新建测试分类标签操作！')
        self.log.info('开始进行新建测试分类操作.')
        cla.click_new_add_class_btn()
        time.sleep(1)
        self.assertEqual('新增分类', cla.text_check_open_add_page(), '弹框没有弹出，请检查！')
        self.log.info('新增分类页弹出成功.')
        cla.input_new_class_name('test')
        cla.click_sure_btn()
        class_name = cla.elements_check_new_add_success()
        for element in class_name:
            if element.text == 'test':
                self.log.info('新增 {} 分类成功.'.format(element.text))


if __name__ == '__main__':
    unittest.main()
