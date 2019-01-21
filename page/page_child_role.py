#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildRolePage(Crazy):
    """角色管理"""
    role_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[10]/div/span')

    def click_role_manage(self):
        self.click(self.role_manage_loc)

    # 二级分类
    all_manage_loc = ('xpath', '//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li/a')

    def elements_all_manage(self):
        return self.find_elements(self.all_manage_loc)

    # 验证
    check_role_text_loc = ('xpath', '//div[@class="bread___2EMeU"]/div/span[2]/span[1]/span')

    def text_check_role_text(self):
        return self.get_text(self.check_role_text_loc)

    # 新增按钮
    new_add_role_btn_loc = ('xpath', '//button[@class="ant-btn ant-btn-primary"]')

    def click_new_add_role_btn(self):
        self.click(self.new_add_role_btn_loc)

    # 验证
    check_text_role_loc = ('xpath', '//div[@class="ant-modal-header"]')

    def text_check_text_role(self):
        return self.get_text(self.check_text_role_loc)

    # 角色名称
    new_role_name_loc = ('id', 'name')

    def input_new_role_name(self, name):
        self.send_keys(self.new_role_name_loc, name)

    # 权限设置
    new_role_config_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/div/label/span[1]/input')

    def elements_new_role_config(self):
        return self.find_elements(self.new_role_config_loc)

    # 确定按钮
    sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 取消按钮
    cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    # 角色名称
    role_name_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[2]')

    def elements_role_name(self):
        return self.find_elements(self.role_name_loc)

    # 设置权限按钮
    set_power_btn_loc = ('xpath', '//tbody[@class="ant-table-tbody"]/tr/td[3]/div/button')

    def elements_set_power_btn(self):
        return self.find_elements(self.set_power_btn_loc)

    # 翻页
    random_skip_page_loc = ('xpath', '//div[@class="ant-pagination-options-quick-jumper"]/input')

    def input_skip_page(self, num):
        self.send_keys(self.random_skip_page_loc, num)

    page_num_loc = ('xpath', '//div[@class="ant-spin-container"]/ul/li')

    def elements_page_num(self):
        return self.find_elements(self.page_num_loc)

    # 标签数量
    tag_number_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[1]')

    def text_tag_number(self):
        return self.get_text(self.tag_number_loc)

    # 选择的权限名称
    check_role_name_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/div/label/span[2]')

    def elements_check_role_name(self):
        return self.find_elements(self.check_role_name_loc)

    # 是否选中
    check_is_checked_loc = (
        'xpath', '//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/div/label/span[1]')

    def elements_check_is_checked(self):
        return self.find_elements(self.check_is_checked_loc)

    # 查询
    query_info_loc = ('id', 'queryString')

    def input_query_info(self, text):
        self.send_keys(self.query_info_loc, text)

    # 查询按钮
    query_info_btn_loc = ('xpath', '//button[@class="ant-btn margin-right ant-btn-primary"]')

    def click_query_info_btn(self):
        self.click(self.query_info_btn_loc)

    # 点击下一页

    next_page_loc = ('xpath', '//ul[@class="ant-pagination ant-table-pagination"]/li[last() - 1]')

    def click_next_page(self):
        self.click(self.next_page_loc)