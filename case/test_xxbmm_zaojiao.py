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


# from common import readConfig
# from common.connectDB import SqL


class TestXbu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.zao = Zaojiaopage(cls.driver)
        cls.t = TouchAction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_authorization(self):
        z = self.zao
        z.swipeDown(n=2)
        if not z.element_zao():
            self.log.error('被测小程序不存在！')
            return
        z.click_zao()
        self.log.info('正在进入被测小程序...')
        time.sleep(1)
        z.click_attend_lectures_btn()
        time.sleep(1)
        self.log.info('进行购买核心课操作...')
        z.click_get_to_know_btn()
        z.click_sure_buy_btn()
        buy_money = float(z.text_buy_money().replace('¥', ''))
        if buy_money != 0.01:
            self.log.error('支付金额不是0.01元！{} 元'.format(buy_money))
            return
        self.log.info('支付金额是：{} 元'.format(buy_money))
        z.input_buy_password('802300')
        z.click_success_btn()
        self.log.info('支付完成，进行领取核心课操作...')
        self.receive_curriculum(z)
        z.click_receive_btn()
        self.log.info('领取课程成功！')
        if z.element_know():
            z.click_know()
        z.swipeUp(n=5)
        z.click_all_curriculum_btn()
        time.sleep(2)
        if z.element_curriculum_date_btn():
            self.log.info('查看历史推送成功！')
        time.sleep(1)
        z.back()
        time.sleep(1)
        z.back()
        time.sleep(1)
        z.back()
        time.sleep(1)
        z.click_my()
        self.assertEqual(z.text_my_baby_title(), '个人中心', '进入个人中心失败！')
        self.log.info('进入个人中心成功，开始进行新建宝宝操作...')
        z.click_my_baby()
        z.click_new_baby_btn()
        time.sleep(1)
        z.click_next()
        z.input_baby_name('我的小宝宝')
        z.click_baby_bir_btn()
        time.sleep(1)
        z.click_sure_btn()
        z.click_finish_btn()
        if z.element_new_baby_btn():
            self.log.error('创建宝宝失败，请检查原因！')
            return
        self.log.info('创建宝宝成功.')
        time.sleep(1)
        z.back()
        time.sleep(1)
        z.click_my_home()
        z.click_switch_btn()
        time.sleep(10)

    def receive_curriculum(self, z):
        z.click_check_address_btn()
        if z.elements_addressee():
            self.log.info('地址信息已存在，默认选择第一个地址信息.')
            z.clicks_addressee()
        else:
            self.log.info('地址信息不存在，进行添加地址信息操作...')
            z.click_add_address_btn()
            z.input_name_btn('lee')
            z.input_phone_btn('18700000000')
            z.click_region_btn()
            z.click_sure_btn()
            z.input_detailed_address_btn('朝阳区酒仙桥110号')
            z.click_save_btn()
            self.log.info('添加收货地址完成！')

    def delete_test_small_program(self, z):
        """发现-小程序-判断小程序是否存在并删除"""
        test_small_program = z.element_zaojiao_small_btn()
        if not test_small_program:
            self.log.error('不存在被测试的小程序！')
            return False
        else:
            while True:
                time.sleep(0.5)
                if z.element_zaojiao_small_btn():
                    z.long_press(z.element_zaojiao_small_btn())
                    z.click_delete_small_btn()
                else:
                    self.log.info('测试小程序删除成功！')
                    break
            return True


if __name__ == '__main__':
    unittest.main()
