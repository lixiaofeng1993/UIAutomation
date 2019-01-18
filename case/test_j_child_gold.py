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
from page.page_child_gold import ChildGoldPage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config


class Testcla(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.gold = ChildGoldPage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_gold')
    def test_a_gold(self):
        """进入金币配置"""
        gold = self.gold
        gold.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        gold.click_gold_manage()
        gold.elements_all_manage()[2].click()
        self.assertEqual(gold.text_check_gold_text(), '金币配置', '进入金币配置栏失败！')
        self.log.info('进入 金币配置 成功.')
        self.save_img('金币配置')

    @BeautifulReport.add_test_img('test_b_new_add_cla')
    def test_b_new_add_cla(self):
        """添加金币配置"""
        gold = self.gold
        self.assertEqual(gold.text_check_gold_text(), '金币配置', '当前页面不在金币配置栏，无法进行添加金币配置操作！')
        self.log.info('开始进行添加金币配置操作.')
        gold.click_new_add_gold_btn()
        time.sleep(1)
        self.assertEqual('选择数据', gold.text_check_data(), '选择数据页面打开失败！')
        self.log.info('选择数据页面打开成功.')
        type_name = gold.elements_new_add_type()
        self.random_check(type_name, gold)
        page_list = gold.elements_check_random_page()
        self.random_check(page_list, gold)
        info_list = gold.elements_check_random_info()
        info_name = self.random_check(info_list, gold, make=2, info=1)[0]
        gold.click_sure_btn()
        if gold.text_new_add_error() == '已存在记录':
            self.log.error('添加重复. {}'.format(info_name))
            return
        time.sleep(1)
        t_num, num = self.get_page_number(gold)
        for i in range(num):
            time.sleep(1)
            already_info_name = gold.elements_page_info_name()
            for element in already_info_name:
                if element.text == info_name:
                    self.log.info('添加金币配置项成功.')
            time.sleep(1)
            gold.click_next_page()

    @BeautifulReport.add_test_img('test_c_edit_cla')
    def test_c_edit_cla(self):
        """编辑金币配置"""
        gold = self.gold
        self.assertEqual(gold.text_check_gold_text(), '金币配置', '当前页面不在金币配置栏，无法进行编辑金币配置操作！')
        self.log.info('开始进行编辑金币配置操作.')
        gold.elements_edit_btn()
        edit_list = gold.elements_edit_btn()
        info_name, random_num = self.random_check(edit_list, gold, make=1)
        gold.click_edit_time()
        time.sleep(1)
        gold.click_now_time()
        text = random.uniform(1, 10)
        gold.input_gold_text(str(round(text, 2)))
        gold.elements_edit_btn()[random_num].click()
        t_num, num = self.get_page_number(gold)
        self.driver.refresh()
        for i in range(num):
            time.sleep(1)
            already_info_name = gold.elements_page_info_name()
            gold_num = gold.elements_gold_num()
            for j in range(len(already_info_name)):
                if already_info_name[j].text == info_name and str((gold_num[j].text)) == str(round(text, 2)):
                    self.log.info('编辑金币配置项成功.  {}，{}'.format(info_name, str(round(text, 2))))
            time.sleep(1)
            gold.click_next_page()

    @BeautifulReport.add_test_img('test_d_delete_cla')
    def test_d_delete_cla(self):
        """删除金币配置"""
        gold = self.gold
        self.assertEqual(gold.text_check_gold_text(), '金币配置', '当前页面不在金币配置栏，无法进行删除金币配置操作！')
        self.log.info('开始进行删除金币配置操作.')
        delete_list = gold.elements_delete_gold_btn()
        info_name, random_num = self.random_check(delete_list, gold, make=1)
        gold.click_delete_gold_sure_btn()
        t_num, num = self.get_page_number(gold)
        self.driver.refresh()
        make = False
        for i in range(num):
            time.sleep(1)
            already_info_name = gold.elements_page_info_name()
            for element in already_info_name:
                if element.text == info_name:
                    make = True
                    self.log.error('删除金币配置项失败！')
            time.sleep(1)
            gold.click_next_page()
        if not make:
            self.log.info('删除金币配置 {} 成功.'.format(info_name))

    @BeautifulReport.add_test_img('test_e_page_gold')
    def test_e_page_gold(self):
        """金币配置翻页"""
        gold = self.gold
        self.assertEqual(gold.text_check_gold_text(), '金币配置', '当前页面不在金币配置栏，无法进行翻页操作！')
        self.log.info('开始进行翻页操作.')
        t_num, num = self.get_page_number(gold)
        skip_page = int(random.randint(0, num) / 10) + 1  # 取整数 + 1
        if t_num > 10:
            gold.input_skip_page(skip_page)
            gold.send_keys_enter()
            page_num_list = gold.elements_page_num()
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
            self.log.info('金币配置项数量太少，无法切换页面.')

    def get_page_number(self, gold):
        time.sleep(1)
        tag_num = gold.text_tag_number()
        t_nun = int(re.findall('(\d+)', tag_num)[0])
        self.log.info('标签数量是：{}'.format(str(t_nun)))
        num = int(int(t_nun) / 10) + 1
        return t_nun, num

    def random_check(self, lis, gold, make=0, list_name='', info=0):
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
                update_class = gold.elements_page_info_name()[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            elif make == 2:
                update_class = gold.elements_check_info_name()[random_num].text
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
