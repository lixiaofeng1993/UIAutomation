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


class TestArticle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.article = ChildArticlePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_1article')
    def test_1article(self):
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
        self.save_img('文章管理')

    @BeautifulReport.add_test_img('test_2newly_build_article')
    def test_2newly_build_article(self):
        """新建文章"""
        article = self.article
        article.click_newly_btn()
        self.log.info('文章新建中...')
        time.sleep(1)
        article.input_article_title('test')
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
        os.system('D:\\UIAutomation\driver\\upfile1.exe "D:\\UIAutomation\data\\1.jpg"')
        self.log.info('上传图片成功！')
        article.input_link_address('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        article.click_cancel()
        # article.click_sure_btn()
        time.sleep(2)
        self.assertEqual('test', article.text_check_article_name(), '文章没有新建成功！')
        self.log.info('文章： {},创建成功.'.format(article.text_check_article_name()))

    @BeautifulReport.add_test_img('test_3update_class_article')
    def test_3update_class_article(self):
        """批量修改文章分类"""
        article = self.article
        article.click_check_list()
        self.assertEqual(article.text_update_class(), '批量修改分类', '未选中指定文章！')
        self.log.info('选中文章成功，进行修改分类操作.')
        time.sleep(1)
        article.click_update_class()
        time.sleep(2)
        try:
            article.click_choice_class1_1()
            time.sleep(1)
            article.click_choice_class2_2()
            update_class = article.text_choice_class3_3()
            article.click_choice_class3_3()
            article.click_choice_sure_btn1()
        except AttributeError:
            article.click_choice_class1()
            time.sleep(1)
            article.click_choice_class2()
            update_class = article.text_choice_class3()
            article.click_choice_class3()
            article.click_choice_sure_btn()
        time.sleep(1)
        self.assertEqual(article.text_check_class(), update_class, '修改文章分类失败！')
        self.log.info('修改文章分类成功.')

    @BeautifulReport.add_test_img('test_4update_tag_article')
    def test_4update_tag_article(self):
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
        try:
            article.click_age_tag()
            time.sleep(1)
            article.click_others_tag()
            time.sleep(1)
            article.click_tag_sure_btn()
        except AttributeError:
            article.click_age_tag1()
            time.sleep(1)
            article.click_others_tag1()
            time.sleep(1)
            article.click_tag_sure_btn1()
        self.log.info('修改文章标签成功.')

    @BeautifulReport.add_test_img('test_5lower_article')
    def test_5lower_article(self):
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

    @BeautifulReport.add_test_img('test_6page_article')
    def test_6page_article(self):
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
                article.click_top()
                time.sleep(1)
                self.log.info('返回页面顶部.')
        else:
            self.log.info('文章数量太少，无法切换页面.')

    @BeautifulReport.add_test_img('test_7query_article')
    def test_7query_article(self):
        """查询文章"""
        article = self.article
        time.sleep(1)
        self.assertEqual(article.text_article_manage_text(), '文章管理', '不在 文章管理 页面，无法进行查询操作！')
        self.log.info('正在进行文章查询工作...')
        time.sleep(1)
        article.click_query_class1()
        time.sleep(1)
        article.click_query_class2()
        article.click_query_class3()
        article.input_query_string('test')
        article.click_query_btn()
        time.sleep(1)
        self.assertEqual('test', article.text_check_article_name(), '查询失败，没有发现查询文章！')
        self.log.info('文章查询成功.')


if __name__ == '__main__':
    unittest.main()
