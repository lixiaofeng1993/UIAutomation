#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_b_child_article.py
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

frame_num = 0
article_class = 0
update_class = []


class TestArticle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.article = ChildArticlePage(cls.driver)
        cls.login = ChildLoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path  # 必须是这个路径
        cls.lower = False

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

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
        article.input_article_title('这是一篇测试文章')
        time.sleep(1)
        article.click_article_author()
        author_list = article.elements_article_author()
        self.random_check(author_list, list_name='author_list')
        time.sleep(1)
        article.click_article_class1()
        time.sleep(1)
        article_class_list = article.elements_article_class2()
        self.random_check(article_class_list, list_name='article_class_list')
        time.sleep(1)
        article_class_list1 = article.elements_article_class3()
        self.random_check(article_class_list1, list_name='article_class_list1')
        list_style = article.elements_new_list_style()
        style = self.random_check(list_style, make=1, list_name='list_style')
        if style:
            # 上传图片
            for i in range(3):
                time.sleep(1)
                article.click_up_img()
                uploaded()
        else:
            article.click_up_img()
            uploaded()
        time.sleep(1)
        article.click_new_tag()
        time.sleep(1)
        article.input_new_input_tag('test')
        article.send_keys_enter()
        age_tag_list = article.elements_new_age_tag()
        self.random_check(age_tag_list, list_name='age_tag_list')
        other_tag_list = article.elements_other_age_tag()
        self.random_check(other_tag_list, list_name='other_tag_list')
        frame_list = article.elements_frame_age_tag()
        global frame_num
        frame_num = self.random_check(frame_list, make=1, list_name='frame_list')
        article.input_link_address('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        # article.click_cancel()
        article.click_sure_btn()
        time.sleep(1)
        if frame_num == 0:
            pass
        else:
            article.click_lower_btn()
            if self.check_lower_btn(article):
                self.log.info('选中下架中按钮成功.')
            else:
                self.log.error('没有选中下架中按钮！')
                return
        self.check_article_new_success(article, '这是一篇测试文章')

    @BeautifulReport.add_test_img('test_c_edit_article')
    def test_c_edit_article(self):
        """编辑文章"""
        article = self.article
        self.switch_self(article, 1, make=1)
        article.move_edit_option()
        time.sleep(1)
        self.assertEqual('编辑文章', article.text_check_newly(), '没有进入编辑文章页面！')
        self.log.info('文章编辑中...')
        time.sleep(1)
        article.input_article_title('做了父母，我们更要相爱')
        time.sleep(1)
        article.click_article_author()
        author_list = article.elements_article_author()
        self.random_check(author_list, list_name='author_list')
        time.sleep(1)
        article.click_article_class1()
        time.sleep(1)
        article_class_list = article.elements_article_class2()
        self.random_check(article_class_list, list_name='article_class_list')
        time.sleep(1)
        article_class_list1 = article.elements_article_class3()
        self.random_check(article_class_list1, list_name='article_class_list1')
        list_style = article.elements_new_list_style()
        style = self.random_check(list_style, make=1, list_name='list_style')
        if style:
            # 上传图片
            for i in range(3):
                article.click_up_img()
                uploaded()
        else:
            article.click_up_img()
            uploaded()
        time.sleep(1)
        article.click_edit_tag()
        time.sleep(1)
        article.input_edit_input_tag('test1')
        article.send_keys_enter()
        age_tag_list = article.elements_new_age_tag()
        self.random_check(age_tag_list, list_name='age_tag_list')
        other_tag_list = article.elements_other_age_tag()
        self.random_check(other_tag_list, list_name='other_tag_list')
        frame_list = article.elements_frame_age_tag()
        global frame_num
        frame_num = self.random_check(frame_list, make=1, list_name='frame_list')
        article.input_link_address('https://mp.weixin.qq.com/s/w0dTikK5q7ov0AbPkQYM5g')
        # article.click_cancel()
        article.click_sure_btn()
        time.sleep(1)
        if frame_num == 0:
            pass
        else:
            article.click_lower_btn()
            if self.check_lower_btn(article):
                self.log.info('选中下架中按钮成功.')
            else:
                self.log.error('没有选中下架中按钮！')
                return
        self.check_article_new_success(article, '做了父母，我们更要相爱')

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
        article_class_list = article.elements_article_class2()
        global article_class, update_class
        article_class = self.random_check(article_class_list, list_name='article_class_list', make=1)
        time.sleep(1)
        article_class_list1 = article.elements_article_class3()
        update_class = self.random_check(article_class_list1, make=2, list_name='article_class_list1')
        self.log.info('修改后的分类名称是：{}'.format(update_class[0]))
        article.click_sure_btn()
        time.sleep(1)
        self.assertEqual(article.text_check_class(), update_class[0], '修改文章分类失败！')
        self.log.info('修改文章分类成功.')

    @BeautifulReport.add_test_img('test_e_update_tag_article')
    def test_e_update_tag_article(self):
        """修改文章标签"""
        article = self.article
        article.click_check_list()
        self.assertEqual(article.text_update_tag(), '批量修改标签', '未选中指定文章！')
        self.log.info('选中文章成功，进行修改标签操作.')
        time.sleep(1)
        article.click_update_tag()
        time.sleep(1)
        age_tag_list = article.elements_age_tag()
        self.random_check(age_tag_list, list_name='age_tag_list')
        time.sleep(1)
        other_tag_list = article.elements_others_tag()
        self.random_check(other_tag_list, list_name='other_tag_list')
        time.sleep(1)
        article.click_sure_btn()
        self.log.info('修改文章标签成功.')

    @BeautifulReport.add_test_img('test_f_lower_article')
    def test_f_lower_article(self):
        """文章跳转"""
        article = self.article
        handle = article.current_window_handle()
        time.sleep(1)
        article_name = article.text_article_name()
        self.log.info('跳转前的文章名称：{}'.format(article_name))
        article.click_article_name()
        article.switch_window_handle(1)
        self.log.info('跳转后的文章名称： {}'.format(article.text_activity_name()))
        self.assertEqual(article_name, article.text_activity_name(), '文章跳转错误！')
        self.log.info('文章链接跳转成功.')
        article.close()
        article.switch_window_handle(handle)
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
        article.click_query_class()
        time.sleep(1)
        global article_class, update_class
        article.elements_query_class1()[article_class + 1].click()
        article.elements_article_class3()[update_class[1]].click()
        article.input_query_string('做了父母，我们更要相爱')
        article.click_query_btn()
        time.sleep(1)
        self.assertEqual('做了父母，我们更要相爱', article.text_check_article_name(), '查询失败，没有发现查询文章！')
        self.log.info('文章查询成功.')

    @BeautifulReport.add_test_img('test_i_delete_article')
    def test_i_delete_article(self):
        """删除文章"""
        article = self.article
        self.assertEqual(article.text_article_manage_text(), '文章管理', '不在 文章管理 页面，无法进行查询操作！')
        self.log.info('正在进行删除文章操作...')
        if not self.check_lower_btn(article):
            self.switch_self(article, 0)
        article.move_delete_option()
        time.sleep(1)
        article.click_lower_sure_btn()
        time.sleep(1)
        article_list_lower = article.elements_get_all_article_name()
        make = False
        for element in article_list_lower:
            if element.text == '做了父母，我们更要相爱':
                make = True
        self.assertEqual(make, False, '删除文章失败！')
        self.log.info('做了父母，我们更要相爱 文章删除成功！')

    def random_check(self, lis, make=0, list_name=''):
        """随机点击元素"""
        if isinstance(lis, list):
            random_num = random.randint(0, len(lis) - 1)
            if not lis[random_num].is_displayed():
                random_num = 6
            if make == 2:
                update_class = lis[random_num].text
            lis[random_num].click()
            self.log.info('{} 随机选择元素：{}'.format(list_name, random_num))
            if make == 1:
                return random_num
            elif make == 2:
                return [update_class, random_num]

        else:
            self.log.error('random_check函数传参错误！')

    def check_lower_btn(self, article):
        """是否选中下架中按钮"""
        lower_btn = article.elements_check_lower_btn()
        for element in lower_btn:
            if element.text == '下架中' and 'checked' in element.get_attribute('class'):
                return True

    def check_article_new_success(self, article, name):
        """检查新建、编辑是否成功"""
        for element in article.elements_check_article_name():
            if element.text == name:
                self.log.info('文章新建/编辑成功.')

    def switch_self(self, article, num, make=0):
        global frame_num
        if frame_num == num:
            article.move_upper_option()  # 上架中文章做下架操作
            time.sleep(1)
            article.click_lower_sure_btn()
            self.log.info('正在切换上下架中. {}'.format(num))
            time.sleep(1)
            if make == 1:
                article.click_upper_btn()
            else:
                article.click_lower_btn()
            time.sleep(1)
        else:
            self.log.info('不用执行切换下架中操作. {}'.format(num))


if __name__ == '__main__':
    unittest.main()
