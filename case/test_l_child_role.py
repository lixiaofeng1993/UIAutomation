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
from page.page_child_role import ChildRolePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class Testcla(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.role = ChildRolePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_role')
    def test_a_role(self):
        """进入角色管理"""
        role = self.role
        role.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        role.click_role_manage()
        role.elements_all_manage()[1].click()
        self.assertEqual(role.text_check_role_text(), '角色管理', '进入角色管理栏失败！')
        self.log.info('进入 角色管理 成功.')
        self.save_img('角色管理')

    @BeautifulReport.add_test_img('test_b_new_add_cla')
    def test_b_new_add_cla(self):
        """添加角色管理"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行添加角色管理操作！')
        self.log.info('开始进行添加角色管理操作.')


    @BeautifulReport.add_test_img('test_e_page_role')
    def test_e_page_role(self):
        """角色管理翻页"""
        role = self.role
        self.assertEqual(role.text_check_role_text(), '角色管理', '当前页面不在角色管理栏，无法进行翻页操作！')
        self.log.info('开始进行翻页操作.')
        t_num, num = self.get_page_number(role)
        skip_page = int(random.randint(0, num) / 10) + 1  # 取整数 + 1
        if t_num > 10:
            role.input_skip_page(skip_page)
            role.send_keys_enter()
            page_num_list = role.elements_page_num()
            for element in page_num_list:
                class_name = element.get_attribute('class')
                if 'ant-pagination-item-active' in class_name:
                    title = element.get_attribute('title')  # 取出当前页面选中的页数
                    self.assertEqual(skip_page, int(title), '跳转页面失败！')
                    self.log.info('跳转页面成功.')
            if len(page_num_list) > 3:
                time.sleep(1)
                page_num_list[1].click()
                time.sleep(1)
                page_num_list[-2].click()
                self.log.info('切换页面完成.')
        else:
            self.log.info('角色管理项数量太少，无法切换页面.')

    def get_page_number(self, role):
        time.sleep(1)
        tag_num = role.text_tag_number()
        t_nun = int(re.findall('(\d+)', tag_num)[0])
        self.log.info('标签数量是：{}'.format(str(t_nun)))
        num = int(int(t_nun) / 10) + 1
        return t_nun, num

    def random_check(self, lis, role, make=0, list_name='', info=0):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
            self.log.info('传入list长度：{}'.format(len(lis)))
            if info == 1:
                random_num = random.randint(0, len(lis) - 2)
            else:
                random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 6
            if make == 1:
                update_class = role.elements_page_info_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            elif make == 2:
                update_class = role.elements_check_info_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            time.sleep(1)
            if make in [1, 2]:
                return [update_class, random_num]
        else:
            self.log.error('random_check函数传参错误！')


if __name__ == '__main__':
    unittest.main()
