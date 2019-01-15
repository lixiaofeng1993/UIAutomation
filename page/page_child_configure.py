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
    configure_manage_loc = ('xpath', '//div[@class="ant-layout-sider-children"]/div/ul/li[7]/a')

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
