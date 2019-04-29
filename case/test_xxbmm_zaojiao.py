#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:22
# @Author  : lixiaofeng
# @File    : test_xxbmm_zaojiao.py
# @Software: PyCharm
# @desc    :

import time
import unittest, random
from faker import Faker
from BeautifulReport import BeautifulReport
from appium.webdriver.common.touch_action import TouchAction
from common.basics import open_app
from common.logger import Log, img_path
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
        cls.faker = Faker('zh_CN')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_1first_baby')
    def test_1first_baby(self):
        """第一个宝宝的购买和领课流程"""
        z = self.zao
        # z.swipeDown(n=2)
        # if not z.element_zao():
        #     self.log.error('被测小程序不存在！')
        #     return
        # z.click_zao()
        # self.log.info('正在进入被测小程序...\n')
        # self.log.info('第一个宝宝开始进行操作...')
        # self.buy_class(z)
        # self.leading_class(z, n=1)
        # self.create_baby(z)
        # self.my_page_operation(z, n=1)
        # self.log.info('第一个宝宝操作完成！\n')

    # @BeautifulReport.add_test_img('test_2second_baby')
    # def test_2second_baby(self):
    #     """第二个宝宝的购买和领课流程"""
    #     z = self.zao
    #     self.log.info('第二个宝宝开始进行操作...')
    #     self.buy_class(z)
    #     self.leading_class(z, n=2)
    #     self.create_baby(z)
    #     self.my_page_operation(z, n=2)
    #     self.log.info('第二个宝宝操作完成！\n')
    #
    # @BeautifulReport.add_test_img('test_3last_baby')
    # def test_3last_baby(self):
    #     """第三个宝宝的购买和领课流程"""
    #     z = self.zao
    #     self.log.info('第三个宝宝开始进行操作...')
    #     self.buy_class(z)
    #     self.leading_class(z, n=3)
    #     self.my_page_operation(z, n=3)
    #     self.log.info('第三个宝宝操作完成！\n')

    def buy_class(self, z):
        """购买流程"""
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

    def leading_class(self, z, n):
        """领取已购买课程，并查看历史推送"""
        self.receive_curriculum(z)
        self.choice_moth(z, n)
        z.click_receive_btn()
        self.log.info('领取课程成功！')
        if z.element_know():
            z.click_know()
        z.swipeUp(n=5)
        z.click_all_curriculum_btn()
        time.sleep(2)
        if z.element_curriculum_date_btn():
            self.log.info('查看历史推送成功！')
        else:
            self.log.error('查看历史推送失败！')
            return
        self.class_info(z, n)
        self._back(z)

    def choice_moth(self, z, n):
        """区别三个宝宝，选择不同的月份"""
        if n == 1:
            pass
        elif n == 2:
            z.click_baby_bri()
            time.sleep(1)
            z.click_mouth_btn()
            z.click_sure_btn()
        else:
            z.click_baby_bri()
            time.sleep(1)
            z.click_mouth_btn()
            time.sleep(1)
            z.click_mouth_btn()
            time.sleep(1)
            z.click_mouth_btn()
            z.click_sure_btn()

    def class_info(self, z, n):
        """操作课程详情页功能"""
        if n == 1:
            z.click_class_name()
            self.log.info('选择指定课程.')
            z.swipeUp(n=5)
            time.sleep(2)
            z.click_collection_btn()
            self.log.info('点击收藏按钮.')
            time.sleep(3)
            self.log.info('进行发布记录操作...')
            z.click_write_record_btn()
            z.input_write_text(self.faker.text(max_nb_chars=200))
            time.sleep(1)
            z.click_album_btn()
            n = random.randint(1, 9)
            for i in range(n):
                z.clicks_choice_album(i)
            self.log.info('选择图片完成.')
            z.click_complete_btn()
            z.click_release_btn()
        else:
            z.click_class_name()
            z.swipeUp(n=5)
            time.sleep(2)
            z.click_collection_btn()
            self.log.info('点击收藏按钮.')
            time.sleep(3)
            self.log.info('进行发布视频记录操作...')
            time.sleep(1)
            z.click_write_record_btn()
            z.input_write_text(self.faker.text(max_nb_chars=200))
            z.click_small_video_btn()
            z.clicks_choice_album(0)
            self.log.info('选择视频成功.')
            z.click_complete_btn()
            time.sleep(3)
            z.click_release_btn()
            self.log.info('发布成功')

    def create_baby(self, z):
        """创建宝宝，并返回首页切换最新创建的宝宝"""
        if not z.element_my_btn():
            self.log.error('当前位置不在首页，无法点击 我的 按钮！')
            return
        z.click_my()
        self.assertEqual(z.text_my_baby_title(), '个人中心', '进入个人中心失败！')
        self.log.info('进入个人中心成功，开始进行新建宝宝操作...')
        z.click_my_baby()
        if not z.element_new_baby_btn():
            self.log.error('无法创建宝宝，请检查原因！')
            return
        z.click_new_baby_btn()
        time.sleep(1)
        z.click_next()
        baby_name = self.faker.last_name()
        z.input_baby_name(baby_name)
        z.click_baby_bir_btn()
        time.sleep(1)
        z.click_sure_btn()
        z.click_finish_btn()
        if z.element_new_baby_btn():
            self.log.error('创建宝宝失败，请检查原因！')
            return
        self.log.info('创建宝宝: {} 成功！'.format(baby_name))
        self._back(z)

    def my_page_operation(self, z, n):
        """我的页面其他功能操作"""
        if not z.element_my_btn():
            self.log.error('当前位置不在首页，无法点击 我的 按钮！')
            return
        z.click_my()
        z.click_my_collection_btn()
        if z.elements_my_collection_english_course_btn():
            if n == len(z.elements_my_collection_english_course_btn()):
                self.log.info('在课程详情页添加收藏成功，共 {} 条！'.format(n))
            else:
                self.log.warning('收藏数量不符！')
        else:
            self.log.warning('在课程详情页添加收藏存在失败的情况，请查明原因！')
        self._back(z)
        z.click_my_course_btn()
        if z.elements_my_course_buy_btn():
            if n == len(z.elements_my_course_buy_btn()):
                self.log.info('成功购买 {} 节早教核心课！'.format(n))
            else:
                self.log.warning('购买早教核心课数量出现错误！')
        self._back(z)
        z.click_my_order_btn()
        if z.elements_my_order_card_btn():
            for i in z.elements_my_order_card_btn():
                self.log.info('获取到的订单编号有： {}'.format(i.text.replace('订单编号：', '')))
        else:
            self.log.warning('未发现订单，请检查原因！')
        self._back(z)
        z.click_my_record_btn()
        if z.elements_my_record_class_btn():
            if n == len(z.elements_my_record_class_btn()):
                self.log.info('成长记录添加成功，共 {} 条！'.format(n))
            else:
                self.log.warning('成长记录添加存在失败的情况，请查看原因！')
        self._back(z)
        z.click_my_home()
        z.click_switch_btn()

    def receive_curriculum(self, z):
        """选择地址信息"""
        z.click_check_address_btn()
        if z.elements_addressee():
            self.log.info('地址信息已存在，默认选择第一个地址信息.')
            z.clicks_addressee()
        else:
            self.log.info('地址信息不存在，进行添加地址信息操作...')
            z.click_add_address_btn()
            z.input_name_btn(self.faker.name())
            z.input_phone_btn(self.faker.phone_number())
            z.click_region_btn()
            z.click_sure_btn()
            z.input_detailed_address_btn(self.faker.address())
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

    def _back(self, z):
        """返回按钮"""
        n = 0
        while True:
            if z.element_back_btn():
                z.click_back_btn()
                self.log.info('连续点击返回操作次数: {}'.format(n))
                n += 1
                if n > 5:
                    z.back()
                    break
            else:
                break


if __name__ == '__main__':
    unittest.main()
