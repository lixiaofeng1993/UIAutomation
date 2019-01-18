#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:42
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_article.py
# @Software: PyCharm

from common.basics import Crazy


class ChildClassPage(Crazy):
    """分类管理"""
    cla_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[7]/div/span')

    def click_cla_manage(self):
        self.click(self.cla_manage_loc)

    # 二级分类
    all_manage_loc = ('xpath', '//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li/a')

    def elements_all_manage(self):
        return self.find_elements(self.all_manage_loc)

    # 验证
    check_cla_text_loc = ('xpath', '//div[@class="bread___2EMeU"]/div/span[2]/span[1]/span')

    def text_check_cla_text(self):
        return self.get_text(self.check_cla_text_loc)

    # 新增分类按钮
    new_add_class_btn_loc = ('xpath', '//div[@class="ant-row"]/div[1]/button')

    def click_new_add_class_btn(self):
        self.click(self.new_add_class_btn_loc)

    # 验证
    check_open_add_page_loc = ('xpath', '//div[@class="ant-modal-title"]')

    def text_check_open_add_page(self):
        return self.get_text(self.check_open_add_page_loc)

    # 选择父节点
    check_parent_node_loc = ('xpath', '//span[@class="ant-select ant-select-enabled ant-select-allow-clear"]/span')

    def click_check_parent_node(self):
        self.click(self.check_parent_node_loc)

    new_class_name_loc = ('id', 'name')

    def input_new_class_name(self, test):
        self.send_keys(self.new_class_name_loc, test)

    # 确定按钮
    sure_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # 取消按钮
    cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    # 验证新增成功
    check_new_add_success_loc = ('xpath', '//ul[@class="ant-tree ant-tree-show-line"]/li/span[2]/span')

    def elements_check_new_add_success(self):
        return self.find_elements(self.check_new_add_success_loc)
