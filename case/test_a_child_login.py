#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 11:55
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_a_child_login.py
# @Software: PyCharm

import unittest
import time, os
from BeautifulReport import BeautifulReport
import paramunittest
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


# /html/body/div[2]/div/span/div/div/div/span
@paramunittest.parametrized(
    {'user': '18701137212', 'psw': '123456'},
    # {'user': 'lixiaofeng', 'psw': 'fengzi80230'},
    # {'user': 'python', 'psw': 'fengzi80230'},
    # {'user': 'java', 'psw': 'fengzi80230'},
    # {'user': 'lal', 'psw': 'fengzi80230'},
    # {'user': 'demaxiy', 'psw': 'fengzi80230'},
    # {'user': '德玛西亚', 'psw': 'fengzi80230'},
    # {'user': '哈哈', 'psw': 'fengzi80230'},
    {'user': 'test001', 'psw': '123456'},
)
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setParameters(self, user, psw):
        self.user = user
        self.psw = psw

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_login')
    def test_login(self):
        """登录"""
        login = self.login
        login.open(self.url, t='育儿锦囊后台管理系统')
        self.log.info('输入用户名和密码...')
        login.input_user(self.user)
        login.input_password(self.psw)
        login.click_login_btn()
        time.sleep(1)
        error = login.text_login_error()
        if error:
            self.log.info('登录报错：{}'.format(error))
        else:
            self.assertEqual(self.user, login.text_check_login(), '用户登录失败！')
            self.log.info('用户: {} 登录成功.'.format(self.user))
            self.save_img('用户登录成功')


if __name__ == '__main__':
    unittest.main()
