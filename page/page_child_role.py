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
