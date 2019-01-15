#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 10:35
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_h_child_configure.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_configure import ChildConfigurePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class TestConfigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.configure = ChildConfigurePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_configure')
    def test_a_configure(self):
        """进入标签管理"""
        configure = self.configure
        configure.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        configure.click_configure_manage()
        configure.elements_all_manage()[0].click()
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '进入标签管理栏失败！')
        self.log.info('进入 标签管理 成功.')
        self.save_img('标签管理')

    @BeautifulReport.add_test_img('test_b_newly_user_tag_configure')
    def test_b_newly_user_tag_configure(self):
        """新建用户标签"""
        configure = self.configure
        self.assertEqual(configure.text_check_configure_text(), '标签管理', '当前页面不在标签管理栏，无法进行新建用户标签操作！')
        self.log.info('开始进行新建用户标签操作.')
        configure.click_newly_tag_btn()
        time.sleep(1)
        self.assertEqual('新增标签', configure.text_check_newly_tag(), '没有弹出新增标签弹框！')
        self.log.info('新增标签弹框显示正常.')
        configure.click_tag_type()
        configure.elements_check_tag_type()[0].click()
        self.log.info('选择用户标签.')
        configure.input_tag_name('test')
        configure.click_upload_sure_btn()
        time.sleep(1)

