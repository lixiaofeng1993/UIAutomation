#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildConfigurePage(Crazy):
    """配置管理"""
    configure_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[7]/div/span')

    def click_configure_manage(self):
        self.click(self.configure_manage_loc)

    # 二级分类
    all_manage_loc = ('xpath', '//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li/a')

    def elements_all_manage(self):
        return self.find_elements(self.all_manage_loc)

    # 验证
    check_configure_text_loc = ('xpath', '//div[@class="bread___2EMeU"]/div/span[2]/span[1]/span')

    def text_check_configure_text(self):
        return self.get_text(self.check_configure_text_loc)

    # 新增标签按钮
    newly_tag_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def click_newly_tag_btn(self):
        self.click(self.newly_tag_btn_loc)

    # 验证弹出新增标签弹框
    check_newly_tag_loc = ('xpath', '//div[@class="ant-modal-title"]')

    def text_check_newly_tag(self):
        return self.get_text(self.check_newly_tag_loc)

    # 标签类型
    tag_type_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[1]/div[2]/div/span/div/div')

    def click_tag_type(self):
        self.click(self.tag_type_loc)

    # 选择标签类型
    check_tag_type_loc = ('xpath',
                          '//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]/li')

    def elements_check_tag_type(self):
        return self.find_elements(self.check_tag_type_loc)

    # 标签名称
    tag_name_loc = ('xpath', '//span[@class="ant-form-item-children"]/input')

    def input_tag_name(self, name):
        self.send_keys(self.tag_name_loc, name)

    # 确定按钮
    upload_sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_upload_sure_btn(self):
        self.click(self.upload_sure_btn_loc)

    # 取消按钮
    upload_cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_upload_cancel_btn(self):
        self.click(self.upload_cancel_btn_loc)

    # 标签重复提示
    tag_already_exist_error_loc = ('xpath', '//div[@class="ant-message-notice"]/div/div/span')

    def text_tag_already_exist_error(self):
        return self.get_text(self.tag_already_exist_error_loc)

    # 已存在的标签名称
    already_exist_tag_name_loc = ('xpath', '//div[@class="ant-table-body"]/table/tbody/tr/td[2]')

    def elements_already_exist_tag_name(self):
        return self.find_elements(self.already_exist_tag_name_loc)

    # 存在标签属于的标签类型
    exist_tag_type_loc = ('xpath', '//div[@class="ant-table-body"]/table/tbody/tr/td[3]')

    def elements_exist_tag_type(self):
        return self.find_elements(self.exist_tag_type_loc)

    # 标签数量
    tag_number_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[1]')

    def text_tag_number(self):
        return self.get_text(self.tag_number_loc)

    # 点击下一页
    next_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last()-1]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    delete_sure_btn_loc = ('xpath', '//div[@class="ant-confirm-btns"]/button[2]')

    def click_delete_sure_btn(self):
        self.click(self.delete_sure_btn_loc)

    # 翻页
    random_skip_page_loc = ('xpath', '//div[@class="ant-pagination-options-quick-jumper"]/input')

    def input_skip_page(self, num):
        self.send_keys(self.random_skip_page_loc, num)

    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)

    # 查询
    query_text_loc = ('id', 'tag')

    def input_text(self, text):
        self.send_keys(self.query_text_loc, text)

    # 查询按钮
    query_btn_loc = ('xpath', '//button[@class="ant-btn margin-right ant-btn-primary"]')

    def click_query_btn(self):
        self.click(self.query_btn_loc)
