#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 11:17
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_f_child_message.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_message import ChildMessagePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class TestMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.message = ChildMessagePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_message')
    def test_a_message(self):
        """进入留言管理"""
        message = self.message
        message.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        message.click_message_manage()
        self.assertEqual(message.text_check_message_text(), '留言管理', '进入留言管理栏失败！')
        self.log.info('进入 留言管理 成功.')
        self.save_img('留言管理')

    @skip
    @BeautifulReport.add_test_img('test_b_to_be_audited_message')
    def test_b_to_be_audited_message(self):
        """待审核留言内容"""
        message = self.message
        self.assertEqual(message.text_check_message_text(), '留言管理', '当前页面不在 留言管理 栏！')
        self.log.info('待审核留言操作开始.')
        if not self.get_message_num(message):
            return
        stay_message_info = message.elements_message_info()
        to_success_examine_message = stay_message_info[0].text
        message.move_option_to_examine()
        self.log.info('待审核留言，审核通过操作.{}'.format(to_success_examine_message))
        time.sleep(1)
        message.click_sure_btn()
        self.check_status(message, status=1)
        self.verification_option_success(message, to_success_examine_message)
        # 批量审核不通过留言
        self.check_status(message)
        choice_message = message.elements_choice_message()
        to_not_examine_message = self.random_check(choice_message, message, make=3, list_name='choice_message')[0]
        self.assertTrue(message.element_check_choice_message(), '批量勾选失败！')
        self.log.info('批量勾选成功，待审核留言，审核不通过操作.{}.'.format(to_not_examine_message))
        message.element_check_choice_message().click()
        time.sleep(1)
        message.click_choice_sure_btn()
        time.sleep(1)
        message.input_to_not_examine_reason('测试审核不通过.')
        message.click_upload_sure_btn()
        self.check_status(message, status=2)
        self.verification_option_success(message, to_not_examine_message)

    @BeautifulReport.add_test_img('test_c_to_not_audited_message')
    def test_c_to_not_audited_message(self):
        """审核不通过留言"""
        message = self.message
        self.assertEqual(message.text_check_message_text(), '留言管理', '当前页面不在 留言管理 栏！')
        self.log.info('审核不通过留言操作开始.')
        self.check_status(message, status=2)
        if not self.get_message_num(message):
            return
        stay_message_info = message.elements_message_info()
        to_success_examine_message = stay_message_info[0].text
        self.log.info('审核不通过留言，审核通过操作.{}'.format(to_success_examine_message))
        message.move_option_to_examine()  # 做审核通过操作
        time.sleep(1)
        message.click_sure_btn()
        self.check_status(message, status=1)
        self.verification_option_success(message, to_success_examine_message)
        # 批量审核通过留言
        self.check_status(message, status=2)
        choice_message = message.elements_choice_message()
        to_not_examine_message = self.random_check(choice_message, message, make=3, list_name='choice_message')[0]
        self.assertTrue(message.element_check_to_success_message(), '批量勾选失败！')
        self.log.info('批量勾选成功，审核不通过留言，审核通过操作.{}.'.format(to_not_examine_message))
        message.element_check_to_success_message().click()
        time.sleep(1)
        message.click_choice_sure_btn()
        self.check_status(message, status=1)
        self.verification_option_success(message, to_not_examine_message)

    @BeautifulReport.add_test_img('test_d_to_success_audited_message')
    def test_d_to_success_audited_message(self):
        """审核通过留言"""
        message = self.message
        self.assertEqual(message.text_check_message_text(), '留言管理', '当前页面不在 留言管理 栏！')
        self.log.info('审核通过留言操作开始.')
        if not self.get_message_num(message):
            return
        not_message_info = message.elements_message_info()[0].text
        self.log.info('审核通过留言，选择回复操作.{}'.format(not_message_info))
        message.move_option_to_not_examine()  # 回复留言
        time.sleep(1)
        message.input_reply_message('测试回复留言')
        message.click_upload_sure_btn()
        time.sleep(1)
        self.assertEqual('测试回复留言', message.text_check_reply_message(), '回复留言失败！')
        self.log.info('回复留言成功，回复内容：{}'.format(message.text_check_reply_message()))
        message.move_option_to_examine()
        self.log.info('审核通过留言，审核不通过操作.{}'.format(not_message_info))
        time.sleep(1)
        message.click_sure_btn()
        time.sleep(1)
        message.input_to_not_examine_reason('测试审核不通过.')
        message.click_upload_sure_btn()
        self.check_status(message, status=2)
        self.verification_option_success(message, not_message_info)
        # 批量审核不通过留言
        self.check_status(message, status=1)
        choice_message = message.elements_choice_message()
        to_not_examine_message = self.random_check(choice_message, message, make=3, list_name='choice_message')[0]
        self.assertTrue(message.element_check_choice_message(), '批量勾选失败！')
        self.log.info('批量勾选成功，审核通过留言，审核不通过操作.{}.'.format(to_not_examine_message))
        message.element_check_choice_message().click()
        time.sleep(1)
        message.click_choice_sure_btn()
        time.sleep(1)
        message.input_to_not_examine_reason('测试审核不通过.')
        message.click_upload_sure_btn()
        self.check_status(message, status=2)
        self.verification_option_success(message, to_not_examine_message)

    @BeautifulReport.add_test_img('test_e_query_message')
    def test_e_query_message(self):
        """查询"""
        message = self.message
        self.assertEqual(message.text_check_message_text(), '留言管理', '当前页面不在 留言管理 栏！')
        self.log.info('查询操作开始.')
        self.check_status(message, status=1)
        message.click_query_time()
        time.sleep(1)
        message.click_query_click_year()
        message.click_query_select_year()
        dat_list = message.elements_query_select_day()
        self.random_check(dat_list, message, list_name='dat_list')
        end_list = message.elements_query_end_day()
        self.random_check(end_list, message, list_name='end_list')
        start_time = message.text_start_time()
        self.log.info('选择的开始日期是：{}'.format(start_time))
        start_s = self.format_time(start_time)
        end_time = message.text_end_time()
        self.log.info('选择的结束日期是：{}'.format(end_time))
        end_s = self.format_time(end_time)
        num = self.get_message_num(message)
        self.log.info('查询到的留言数量：{}'.format(num))
        page_num = int(int(num) / 10) + 1
        for i in range(page_num):
            self.check_query_success(message, start_s, end_s)
            message.click_next_page()
            time.sleep(1)

    def check_query_success(self, message, start_s, end_s):
        """验证查询成功"""
        message_time = message.elements_check_message_time()
        for element in message_time:
            message_s = self.format_time(element.text, make=1)
            if start_s < message_s < end_s:
                self.log.info('查询成功，留言日期：{}'.format(element.text))
            else:
                self.log.error('查询失败！{}'.format(element.text))

    def format_time(self, t, make=0):
        """格式化日期"""
        if make:
            ts = time.strptime(t, '%Y-%m-%d %H:%M:%S')
        else:
            ts = time.strptime(t, "%Y-%m-%d")
        s = time.mktime(ts)
        return s

    def check_no_data(self, message):
        """验证是否有数据"""
        if message.elements_message_info():
            return True
        else:
            if message.text_message_data():
                self.log.warning('{}，无法进行相关操作！'.format(message.text_message_data()))
                return False

    def get_message_num(self, message):
        """获取留言数量"""
        if not self.check_no_data(message):
            return False
        else:
            message_num = message.text_message_num()
            nun = int(re.findall('(\d+)', message_num)[0])
            self.log.info('留言数量：{}'.format(nun))
            return nun

    def verification_option_success(self, message, info, make=0):
        """验证操作成功"""
        time.sleep(1)
        num = self.get_message_num(message)
        page_num = int(int(num) / 10) + 1
        for i in range(page_num):
            success_message_info = message.elements_message_info()
            for element in success_message_info:
                if element.text == info:
                    self.log.info('审核通过/未通过留言：{}，操作成功.'.format(element.text))
            message.click_next_page()
            time.sleep(1)

    def check_status(self, message, status=0):
        """选择审核状态"""
        time.sleep(1)
        examine_status = message.elements_examine_status()
        self.log.info('切换审核状态中...{}'.format(status))
        examine_status[status].click()
        if status == 0:
            if examine_status[status].text == '待审核' and 'checked' in examine_status[status].get_attribute('class'):
                self.log.info('选择 待审核 状态成功.')
                time.sleep(1)
                return True
        elif status == 1:
            if examine_status[status].text == '审核通过' and 'checked' in examine_status[status].get_attribute('class'):
                self.log.info('选择 审核通过 状态成功.')
                time.sleep(1)
                return True
        elif status == 2:
            if examine_status[status].text == '审核未通过' and 'checked' in examine_status[status].get_attribute('class'):
                self.log.info('选择 审核未通过 状态成功.')
                time.sleep(1)
                return True
        else:
            self.log.error('status 参数传值错误.')
            return False

    def random_check(self, lis, message, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
            self.log.info('传入list长度：{}'.format(len(lis)))
            random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 6
            if make == 2:
                update_class = lis[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            elif make == 3:
                update_class = message.elements_message_info()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            time.sleep(1)
            if make == 1:
                return random_num
            elif make in [2, 3]:
                return [update_class, random_num]
        else:
            self.log.error('random_check函数传参错误！')


if __name__ == '__main__':
    unittest.main()
