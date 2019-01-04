#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 11:25
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_cps.py
# @Software: PyCharm

import time
import unittest

from common.basics import open_browser
from common.connect_db import SqL
from common.logger import Log
from tmp.eg.page_cps_login import LoginPage


class TestSmithereensMovies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.url = 'https://pintuan.api.xxbmm.com/sharebuy/admin323/admin'
        cls.db = SqL()

    @classmethod
    def tearDownClass(cls):
        cls.login.close()

    def test_login(self):
        login = self.login
        login.open(url=self.url, t='后台管理系统登录')
        login.input_username('adminkf_sql')
        login.input_pass('sql123')
        login.click_login_btn()
        login.click_cps_manage()
        time.sleep(3)
        login.click_user()
        for i in range(6, 20):
            time.sleep(3)
            login.switch_frame(('id', 'childfframe'))
            login.click_user_add()
            time.sleep(3)
            login.switch_frame(('id', 'layui-layer-iframe1'))
            login.input_user_name('李四' + str(i))
            login.input_user_telephone(str(18701137200 + i))
            login.click_submit()


if __name__ == '__main__':
    unittest.main()
