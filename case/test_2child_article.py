#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_2child_article.py
# @Software: PyCharm
import unittest
import time, os, re, random, subprocess
from unittest import skip
from BeautifulReport import BeautifulReport
from page.page_child_article import ChildArticlePage
from page.page_child_login import ChildLoginPage
from common.logger import Log, img_path
from common.basics import open_browser
from common import read_config
from common.random_upload import uploaded


class TestArticle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.article = ChildArticlePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_a_article')
    def test_a_article(self):
        """进入文章管理"""
        article = self.article
        article.open(self.url, t='育儿锦囊后台管理系统')
        self.login.input_user('test001')
        self.login.input_password('123456')
        self.login.click_login_btn()
        time.sleep(3)
        self.assertEqual('test001', self.login.text_check_login(), '用户登录失败！')
        article.click_article_manage()
        self.assertEqual(article.text_article_manage_text(), '文章管理', '进入文章管理栏失败！')
        self.log.info('进入 文章管理 成功.')

    @BeautifulReport.add_test_img('test_b_newly_build_article')
    def test_b_newly_build_article(self):
        """新建文章"""
        article = self.article
        article.click_newly_btn()
        time.sleep(1)
        self.assertEqual('新建文章', article.text_check_newly(), '没有进入新建文章页面！')
        self.log.info('文章新建中...')
        time.sleep(1)
        article.input_article_title('这是一篇测试文章')
        time.sleep(1)
        article.click_article_author()
        article.send_keys_enter()
        time.sleep(1)
        article.click_article_class1()
        time.sleep(1)
        article.click_article_class2()
        article.click_article_class3()
        # 上传图片
        article.click_up_img()
        uploaded()
        self.log.info('上传图片成功！')
        article.input_link_address('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        # article.click_cancel()
        article.click_choice_sure_btn()
        time.sleep(2)
        self.assertEqual('这是一篇测试文章', article.text_check_article_name(), '文章没有新建成功！')
        self.log.info('文章： {},创建成功.'.format(article.text_check_article_name()))

    @BeautifulReport.add_test_img('test_c_edit_article')
    def test_c_edit_article(self):
        """编辑文章"""
        article = self.article
        article.move_edit_option()
        time.sleep(1)
        self.assertEqual('编辑文章', article.text_check_newly(), '没有进入编辑文章页面！')
        self.log.info('文章编辑中...')
        time.sleep(1)
        article.input_article_title('test')
        # 上传图片
        article.click_up_img()
        uploaded()
        article.input_link_address('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        article.click_choice_sure_btn()
        time.sleep(2)
        self.assertEqual('test', article.text_check_article_name(), '文章没有编辑成功！')
        self.log.info('文章： {},编辑成功.'.format(article.text_check_article_name()))

    @BeautifulReport.add_test_img('test_d_update_class_article')
    def test_d_update_class_article(self):
        """批量修改文章分类"""
        article = self.article
        article.click_check_list()
        self.assertEqual(article.text_update_class(), '批量修改分类', '未选中指定文章！')
        self.log.info('选中文章成功，进行修改分类操作.')
        time.sleep(1)
        article.click_update_class()
        time.sleep(1)
        article.click_choice_class1()
        time.sleep(1)
        article.click_choice_class2()
        update_class = article.text_article_class()
        article.click_article_class3()
        article.click_choice_sure_btn()
        time.sleep(1)
        self.assertEqual(article.text_check_class(), update_class, '修改文章分类失败！')
        self.log.info('修改文章分类成功.')

    @BeautifulReport.add_test_img('test_e_update_tag_article')
    def test_e_update_tag_article(self):
        """修改文章标签"""
        article = self.article
        try:
            article.click_check_list()
        except Exception:
            article.click_check_list()
        self.assertEqual(article.text_update_tag(), '批量修改标签', '未选中指定文章！')
        self.log.info('选中文章成功，进行修改标签操作.')
        time.sleep(1)
        article.click_update_tag()
        time.sleep(1)
        article.click_age_tag()
        time.sleep(1)
        article.click_others_tag()
        time.sleep(1)
        article.click_choice_sure_btn()
        self.log.info('修改文章标签成功.')

    @BeautifulReport.add_test_img('test_f_lower_article')
    def test_f_lower_article(self):
        """文章跳转"""
        article = self.article
        article.click_lower_btn()
        handle = article.current_window_handle()
        time.sleep(1)
        article_name = article.text_article_name()
        article.click_article_name()
        article.switch_window_handle(1)
        self.assertEqual(article_name, article.text_activity_name(), '文章跳转错误！')
        self.log.info('文章链接跳转成功.')
        article.close()
        article.switch_window_handle(handle)
        article.click_upper()
        self.log.info('返回原页面成功.')

    @BeautifulReport.add_test_img('test_g_page_article')
    def test_g_page_article(self):
        """文章翻页"""
        article = self.article
        page_num = article.text_page_article()
        nun = int(re.findall('(\d+)', page_num)[0])
        if nun > 10:
            skip_page = int(random.randint(0, nun) / 10) + 1  # 取整数 + 1
            article.input_skip_page(skip_page)
            article.send_keys_enter()
            page_num_list = article.elements_page_num()
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
            if article.element_top():
                time.sleep(1)
                article.click_top()
                time.sleep(1)
                self.log.info('返回页面顶部.')
        else:
            self.log.info('文章数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_h_query_article')
    def test_h_query_article(self):
        """查询文章"""
        article = self.article
        time.sleep(1)
        self.assertEqual(article.text_article_manage_text(), '文章管理', '不在 文章管理 页面，无法进行查询操作！')
        self.log.info('正在进行文章查询工作...')
        time.sleep(1)
        article.click_query_class()
        time.sleep(1)
        article.click_query_class1()
        article.click_article_class3()
        article.input_query_string('test')
        article.click_query_btn()
        time.sleep(1)
        self.assertEqual('test', article.text_check_article_name(), '查询失败，没有发现查询文章！')
        self.log.info('文章查询成功.')

    @BeautifulReport.add_test_img('test_i_operation_article')
    def test_i_operation_article(self):
        """下架文章"""
        article = self.article
        self.assertEqual(article.text_article_manage_text(), '文章管理', '不在 文章管理 页面，无法进行查询操作！')
        self.log.info('正在进行文章下架操作...')
        article_list = article.elements_get_all_article_name()
        if article_list[0].text == 'test':
            article.move_lower_option()
            time.sleep(1)
            article.click_lower_sure_btn()
            time.sleep(1)
            article.click_lower_btn()
            time.sleep(1)
            article_list_lower = article.elements_get_all_article_name()
            for element in article_list_lower:
                if element.text == 'test':
                    self.log.info('文章 test 下架成功.')
        else:
            self.log.error('未发现文章 test，无法进行下架操作！')

    @BeautifulReport.add_test_img('test_j_delete_article')
    def test_j_delete_article(self):
        """删除文章"""
        article = self.article
        self.assertEqual(article.text_article_manage_text(), '文章管理', '不在 文章管理 页面，无法进行查询操作！')
        self.log.info('正在进行删除文章操作...')
        time.sleep(1)
        lower_btn = article.elements_check_lower_btn()
        lower = False
        for element in lower_btn:
            if element.text == '下架中' and 'checked' in element.get_attribute('class'):
                lower = True
                self.log.info('选择下架中按钮成功，进行删除操作.')
        if lower:
            article.move_delete_option()
            time.sleep(1)
            article.click_lower_sure_btn()
            time.sleep(1)
            article_list_lower = article.elements_get_all_article_name()
            make = False
            for element in article_list_lower:
                if element.text == 'test':
                    make = True
            self.assertEqual(make, False, '删除文章失败！')
            self.log.info('test 文章删除成功！')


if __name__ == '__main__':
    unittest.main()
