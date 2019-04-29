#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 11:39
# @Author  : lixiaofeng
# @Site    : 
# @File    : 1test_xxbmm_public.py
# @Software: PyCharm

import time
import unittest
from appium.webdriver.common.touch_action import TouchAction
from common.basics import open_app
from common.logger import Log
from page.page_public import Pulicpage


# from common import readConfig
# from common.connectDB import SqL


class TestXbu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.public = Pulicpage(cls.driver)
        cls.t = TouchAction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_authorization(self):
        public = self.public
        time.sleep(2)
        public.click_find()
        public.click_search_btn()
        public.click_search()
        public.click_small_zao()
        public.click_two_small_zao()
        public.click_follow_public()
        public.click_in_home_zao()
        public.long_press(public.element_qr_code())
        public.click_discern_code()
        self.assertIn('小小包早教训练营', public.text_class_group(), '扫码识别错误！')
        self.log.info('扫码识别成功！')
        time.sleep(1)
        public.back()
        time.sleep(1)
        public.click_back_btn()
        self.assertEqual(public.text_small_zao_title(), '小小包早教', '返回小小包早教公众号首页失败！')
        self.log.info('返回小小包早教公众号成功！')
        public.click_more_btn()
        public.click_not_paying()
        public.click_sure_not_paying()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
