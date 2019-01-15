#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:11
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_g_child_scene.py
# @Software: PyCharm

import unittest
import time, os, re, random
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_scene import ChildScenePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config
from common.random_upload import uploaded

_type = ''
upper_type = 0


class Testscene(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.scene = ChildScenePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_scene')
    def test_a_scene(self):
        """进入情景互动"""
        scene = self.scene
        scene.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        scene.click_scene_manage()
        self.assertEqual(scene.text_check_scene_text(), '情景互动', '进入情景互动栏失败！')
        self.log.info('进入 情景互动 成功.')
        self.save_img('情景互动')

    @BeautifulReport.add_test_img('test_b_newly_scene')
    def test_b_newly_scene(self):
        """新增"""
        scene = self.scene
        self.assertEqual(scene.text_check_scene_text(), '情景互动', '当前页面不在情景互动栏，无法进行新增操作！')
        self.log.info('开始进行新增情景互动操作.')
        scene_type = scene.elements_scene_type()
        global _type
        _type = self.random_check(scene_type, scene, make=1)
        scene.click_scene_newly_btn()
        time.sleep(1)
        self.assertEqual('新增{}类'.format(_type), scene.text_check_newly_text(), '没有弹出新增弹窗！')
        self.log.info('弹出新增弹窗成功，进行新建操作.')
        scene.input_description('test')
        scene.input_popup_title('test标题')
        if _type in ['课程', '文章']:
            scene.click_add_type_info()
            self.check_scene_info(scene)
            scene.input_config_word('test文案')
            if _type == '文章':
                scene.click_upload_img_btn()
                uploaded()
            scene.click_again_add()
            self.check_scene_info(scene)
            scene.input_second_config_word('第二个test文案')
            if _type == '文章':
                scene.click_upload_img_btn()
                uploaded()
            time.sleep(1)
        else:
            for i in range(3):
                ran = random.randint(1000, 9999)
                scene.input_add_goods(ran)
                scene.click_add_btn()
            goods_list = scene.elements_delete_goods_btn()
            self.random_check(goods_list, scene)
            scene.click_delete_sure_btn()
            time.sleep(1)
        upper_list = scene.elements_is_upper_lower()
        global upper_type
        upper_type = self.random_check(upper_list, scene, make=3, list_name='upper_list')
        scene.click_sure_btn()
        time.sleep(1)
        if upper_type == 0:
            for element in scene.elements_scene_page_info():
                if element.text == 'test':
                    self.log.info('新增情景互动信息成功1.')
        elif upper_type == 1:
            scene.elements_upper_lower_btn()[1].click()
            time.sleep(1)
            for element in scene.elements_scene_page_info():
                if element.text == 'test':
                    self.log.info('新增情景互动信息成功.')

    @BeautifulReport.add_test_img('test_c_edit_scene')
    def test_c_edit_scene(self):
        """编辑"""
        scene = self.scene
        self.assertEqual(scene.text_check_scene_text(), '情景互动', '当前页面不在情景互动栏，无法进行编辑操作！')
        self.log.info('开始进行编辑情景互动操作.')
        scene.move_edit_scene_btn()
        time.sleep(1)
        global _type
        self.assertEqual('新增{}类'.format(_type), scene.text_check_newly_text(), '没有弹出新增弹窗！')
        self.log.info('弹出新增弹窗成功，进行编辑操作.')
        scene.input_description('这是一个测试场景')
        scene.input_popup_title('这是一个测试标题')
        if _type in ['课程', '文章']:
            scene.click_add_type_info()
            self.check_scene_info(scene)
            scene.input_config_word('这是一个测试文案')
            if _type == '文章':
                scene.click_upload_img_btn()
                uploaded()
            scene.click_repeat_info_btn()
            self.check_scene_info(scene)
            scene.input_second_config_word('第二个测试文案')
            if _type == '文章':
                scene.click_upload_img_btn()
                uploaded()
            time.sleep(1)
        else:
            for i in range(2):
                ran = random.randint(1000, 9999)
                scene.input_add_goods(ran)
                scene.click_add_btn()
            goods_list = scene.elements_delete_goods_btn()
            self.random_check(goods_list, scene)
            scene.click_delete_sure_btn()
            time.sleep(1)
        upper_list = scene.elements_is_upper_lower()
        global upper_type
        upper_type = self.random_check(upper_list, scene, make=3, list_name='upper_list')
        scene.click_sure_btn()
        time.sleep(1)
        if upper_type == 0:
            for element in scene.elements_scene_page_info():
                if element.text == '这是一个测试场景':
                    self.log.info('编辑情景互动信息成功.')
        elif upper_type == 1:
            scene.elements_upper_lower_btn()[1].click()
            time.sleep(1)
            for element in scene.elements_scene_page_info():
                if element.text == '这是一个测试场景':
                    self.log.info('编辑情景互动信息成功.')

    @BeautifulReport.add_test_img('test_d_option_scene')
    def test_d_option_scene(self):
        """上下架、查看、删除"""
        scene = self.scene
        self.assertEqual(scene.text_check_scene_text(), '情景互动', '当前页面不在情景互动栏，无法进行相关操作！')
        self.log.info('开始进行相关操作.')
        global upper_type, _type
        if upper_type == 0:
            self.log.info('进行查看情景互动操作.')
            time.sleep(1)
            scene.elements_upper_lower_btn()[0].click()
            scene.move_look_scene_btn_loc()
            time.sleep(1)
            self.assertEqual('新增{}类'.format(_type), scene.text_check_newly_text(), '没有弹出查看弹窗！')
            self.log.info('弹出查看弹出成功.')
            scene.click_close_x()
            time.sleep(1)
            self.log.info('进行下架情景互动操作.')
            scene_name = scene.text_scene_name()
            scene.move_upper_scene_btn()
            time.sleep(1)
            scene.click_delete_sure_btn()
            time.sleep(1)
            scene.elements_upper_lower_btn()[1].click()
            time.sleep(1)
            make = False
            for element in scene.elements_scene_page_info():
                if element.text == scene_name:
                    self.log.info('编辑情景互动信息成功. {}'.format(scene_name))
                    make = True
            if make:
                scene.move_delete_scene_btn()
                time.sleep(1)
                scene.click_delete_sure_btn()
                time.sleep(1)
                if not scene.elements_scene_page_info():
                    self.log.info('删除成功. {}'.format(scene_name))
                else:
                    for element in scene.elements_scene_page_info():
                        if element.text == scene_name:
                            self.log.info('删除情景互动信息失败！ {}'.format(scene_name))
        else:
            self.log.info('进行上架情景互动操作.')
            time.sleep(1)
            scene.elements_upper_lower_btn()[1].click()
            scene_name = scene.text_scene_name()
            scene.move_upper_scene_btn()
            time.sleep(1)
            scene.click_delete_sure_btn()
            time.sleep(1)
            scene.elements_upper_lower_btn()[0].click()
            time.sleep(1)
            for element in scene.elements_scene_page_info():
                if element.text == scene_name:
                    self.log.info('上架情景互动信息成功. {}'.format(scene_name))

    @BeautifulReport.add_test_img('test_e_query_scene')
    def test_e_query_scene(self):
        """查询"""
        scene = self.scene
        self.assertEqual(scene.text_check_scene_text(), '情景互动', '当前页面不在情景互动栏，无法进行查询操作！')
        self.log.info('开始进行查询操作.')
        scene.input_query_input('测试')
        scene.click_query_btn()
        for element in scene.elements_scene_page_info():
            if "测试" in element.text:
                self.log.info('查询情景互动信息成功. {}'.format(element.text))

    def check_scene_info(self, scene):
        """选择情景互动内容"""
        time.sleep(1)
        page_list = scene.elements_page_btn()
        time.sleep(1)
        self.random_check(page_list, scene, list_name='page_list')
        info_list = scene.elements_check_scene_info()
        self.random_check(info_list, scene, list_name='info_list')
        scene.click_one_sure_btn()
        time.sleep(1)
        if scene.text_repeat_add_info_error() == '已经添加过该文章':
            self.check_scene_info(scene)
        time.sleep(1)

    def random_check(self, lis, scene, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            time.sleep(1)
            self.log.info('传入list长度：{}'.format(len(lis)))
            random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 0
            if make == 2:
                update_class = lis[random_num].text
                self.log.info('随机点击的元素text：{}'.format(update_class))
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            lis[random_num].click()
            time.sleep(1)
            if make == 1:
                if random_num == 0:
                    return '课程'
                elif random_num == 1:
                    return '文章'
                elif random_num == 2:
                    return '商品'
            elif make == 2:
                return [update_class, random_num]
            elif make == 3:
                return random_num
        else:
            self.log.error('random_check函数传参错误！')


if __name__ == '__main__':
    unittest.main()
