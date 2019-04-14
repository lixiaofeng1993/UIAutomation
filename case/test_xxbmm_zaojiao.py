#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:22
# @Author  : lixiaofeng
# @File    : test_xxbmm_zaojiao.py
# @Software: PyCharm
# @desc    :

import time
import unittest
from appium.webdriver.common.touch_action import TouchAction
from common.basics import open_app
from common.logger import Log
from page.page_zaojiao import Zaojiaopage
from common.operation_excel import Write_excel


# from common import readConfig
# from common.connectDB import SqL


class TestXbu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.z = Zaojiaopage(cls.driver)
        cls.t = TouchAction(cls.driver)
        cls.write = Write_excel('G:\\UIAutomation\data\demo_api.xlsx')
        # cls.db = SqL()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_authorization(self):
        z = self.z
        time.sleep(2)
        # z.clicks_find()
        # time.sleep(1)
        # z.clicks_small()
        # time.sleep(1)
        # if z.element_zaojiao_small_btn():
        #     self.t.long_press(z.element_zaojiao_small_btn()).perform()
        #     time.sleep(1)
        #     z.click_delete_small_btn()
        # else:
        #     z.click_helper()
        #     time.sleep(2)
        #     z.click_edition_btn()
        #     z.click_version_btn()

        z.swipeDown(n=2)
        # z.click_zao()
        time.sleep(5)
        AppNameHold = z.long_press(z.element_zao()) # 长按
        # AppNameHold.move_to(z.element_delete_small1_btn()).release().perform()
        # z.drag_and_drop(z.element_zao(), z.element_edition_btn())
        # print('1111111111111111')
        # z.swipeDown(n=2)
        time.sleep(3)
        # AppNameElment = z.find_element_by_android_uiautomator("new UiSelector().text(\"应用\")")
        # AppNameHold = TouchAction(driver).press(AppNameElment).wait(1000).perform()  # 按住应用图标不放
        # DelElment = driver.find_element_by_android_uiautomator("new UiSelector().text(\"删除\")")  # 找到删除控件
        # AppNameHold.move_to(DelElment).release().perform()  # 拖动应用到删除控件处释放删除


if __name__ == '__main__':
    unittest.main()
