#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildArticlePage(Crazy):
    """文章管理"""
    #                               //*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[2]/a
    article_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[2]/a')

    def click_article_manage(self):
        self.click(self.article_manage_loc)

    # 验证
    article_manage_text_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[1]/div/span/span[1]/span')

    def text_article_manage_text(self):
        return self.get_text(self.article_manage_text_loc)

    # 新建文章按钮
    newly_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div[4]/button')

    def click_newly_btn(self):
        self.click(self.newly_btn_loc)

    # 文章标题
    article_title_loc = ('id', 'title')

    def input_article_title(self, title):
        self.send_keys(self.article_title_loc, title)

    # 文章作者
    article_author_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div')

    def click_article_author(self):
        return self.click(self.article_author_loc)

    # 文章分类
    article_class1_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div[2]/div/span/span/span')

    def click_article_class1(self):
        self.click(self.article_class1_loc)

    article_class2_loc = ('xpath', '/html/body/div[4]/div/div/div/ul[1]/li[2]')

    def click_article_class2(self):
        self.click(self.article_class2_loc)

    article_class3_loc = ('xpath', '/html/body/div[4]/div/div/div/ul[2]/li[1]')

    def click_article_class3(self):
        self.click(self.article_class3_loc)

    # 上传图片
    up_img_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/span/div[1]/span/button')

    def click_up_img(self):
        self.click(self.up_img_loc)

    # 文章url地址
    link_address_loc = ('id', 'linkUrl')

    def input_link_address(self, link):
        self.send_keys(self.link_address_loc, link)

    # 取消按钮
    cancel_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_cancel(self):
        self.click(self.cancel_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 验证新增成功
    check_article_name_loc = (
        'xpath',
        '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/span/a')

    def text_check_article_name(self):
        return self.get_text(self.check_article_name_loc)

    # 查询
    # 分类
    query_class1_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div[1]/span/span')

    def click_query_class1(self):
        self.click(self.query_class1_loc)

    query_class2_loc = ('xpath', '/html/body/div[3]/div/div/div/ul[1]/li[3]')

    def click_query_class2(self):
        self.click(self.query_class2_loc)

    query_class3_loc = ('xpath', '/html/body/div[3]/div/div/div/ul[2]/li[3]')

    def click_query_class3(self):
        self.click(self.query_class3_loc)

    query_string_loc = ('id', 'queryString')

    def input_query_string(self, string):
        self.send_keys(self.query_string_loc, string)

    query_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div[3]/button')

    def click_query_btn(self):
        self.click(self.query_btn_loc)

    # 批量修改分类
    check_list_loc = ('xpath',
                      '//tbody[@class="ant-table-tbody"]/tr[1]/td[1]/span/label/span')

    def click_check_list(self):
        self.click(self.check_list_loc)

    update_class_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div[5]/span/button[1]')

    def text_update_class(self):
        return self.get_text(self.update_class_loc)

    def click_update_class(self):
        self.click(self.update_class_loc)

    # 点不上                       /html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div/div[2]/div/span/span/span
    choice_class1_loc = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div/div[2]/div/span/span')
    choice_class1_1_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div/div[2]/div/span/span/span')

    def click_choice_class1(self):
        self.click(self.choice_class1_loc)

    def click_choice_class1_1(self):
        self.click(self.choice_class1_1_loc)

    #                               /html/body/div[4]/div/div/div/ul/li[2]
    choice_class2_loc = ('xpath', '/html/body/div[4]/div/div/div/ul/li[2]')
    choice_class2_2_loc = ('xpath', '/html/body/div[3]/div/div/div/ul/li[2]')

    def click_choice_class2(self):
        self.click(self.choice_class2_loc)

    def click_choice_class2_2(self):
        self.click(self.choice_class2_2_loc)

    choice_class3_loc = ('xpath', '/html/body/div[4]/div/div/div/ul[2]/li[3]')
    choice_class3_3_loc = ('xpath', '/html/body/div[3]/div/div/div/ul[2]/li[3]')

    def text_choice_class3(self):
        return self.get_text(self.choice_class3_loc)

    def click_choice_class3(self):
        self.click(self.choice_class3_loc)

    def text_choice_class3_3(self):
        return self.get_text(self.choice_class3_3_loc)

    def click_choice_class3_3(self):
        self.click(self.choice_class3_3_loc)

    choice_sure_btn_loc = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[2]')
    choice_sure_btn1_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_choice_sure_btn(self):
        self.click(self.choice_sure_btn_loc)

    def click_choice_sure_btn1(self):
        self.click(self.choice_sure_btn1_loc)

    # 验证
    check_class_loc = (
        'xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]')

    def text_check_class(self):
        return self.get_text(self.check_class_loc)

    # 批量修改标签
    update_tag_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[1]/div[5]/span/button[2]')

    def click_update_tag(self):
        self.click(self.update_tag_loc)

    def text_update_tag(self):
        return self.get_text(self.update_tag_loc)

    age_tag_loc = (
        'xpath',
        '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/span/div/label[1]/span[1]')
    age_tag1_loc = (
        'xpath',
        '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/span/div/label[1]/span[1]')

    def click_age_tag(self):
        self.click(self.age_tag_loc)

    def click_age_tag1(self):
        self.click(self.age_tag1_loc)

    others_tag_loc = (
        'xpath',
        '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div/label[1]/span[1]')
    others_tag1_loc = (
        'xpath',
        '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div/label[1]/span[1]')

    def click_others_tag(self):
        self.click(self.others_tag_loc)

    def click_others_tag1(self):
        self.click(self.others_tag1_loc)

    tag_sure_btn_loc = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[2]')
    tag_sure_btn1_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_tag_sure_btn(self):
        self.click(self.tag_sure_btn_loc)

    def click_tag_sure_btn1(self):
        self.click(self.tag_sure_btn1_loc)

    # 下架文章
    lower_btn_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/label[2]/span[2]')

    def click_lower_btn(self):
        self.click(self.lower_btn_loc)

    article_name_loc = ('xpath',
                        '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/span/a')

    def click_article_name(self):
        self.click(self.article_name_loc)

    def text_article_name(self):
        return self.get_text(self.article_name_loc)

    activity_name_loc = ('id', 'activity-name')

    def text_activity_name(self):
        return self.get_text(self.activity_name_loc).strip()

    upper_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div[2]/div/div/label[1]/span[2]')

    def click_upper(self):
        self.click(self.upper_loc)

    # 翻页
    page_article_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li[1]')

    def text_page_article(self):
        return self.get_text(self.page_article_loc)

    # 跳至
    skip_page_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li[11]/div[2]/input')

    def input_skip_page(self, num):
        self.send_keys(self.skip_page_loc, num)

    # 显示的页数
    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)

    # 返回顶部
    top_loc = ('class name', 'ant-back-top')

    def element_top(self):
        return self.find_element(self.top_loc)

    def click_top(self):
        self.click(self.top_loc)
