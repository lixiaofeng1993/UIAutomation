#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 11:27
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_cps_login.py
# @Software: PyCharm

from common.basics import Crazy


class LoginPage(Crazy):
    """登录模块元素封装"""

    username_loc = ('id', 'username')

    def input_username(self, phone):
        self.send_keys(self.username_loc, phone)

    pass_loc = ('id', 'password')

    def input_pass(self, password):
        self.send_keys(self.pass_loc, password)

    login_btn_loc = ('xpath', '//*[@id="login"]/button')

    def click_login_btn(self):
        self.click(self.login_btn_loc)

    cps_manage_loc = ('xpath', '//*[@id="mian"]/div[1]/div[3]/a[1]')

    def click_cps_manage(self):
        self.click(self.cps_manage_loc)

    user_loc = ('xpath', '//*[@id="mian"]/div[1]/div[3]/a[3]')

    def click_user(self):
        self.click(self.user_loc)

    user_add_loc = ('id', 'add')

    def click_user_add(self):
        self.click(self.user_add_loc)

    user_name_loc = ('id', 'name')

    def input_user_name(self, user):
        self.send_keys(self.user_name_loc, user)

    user_telephone_loc = ('id', 'telephone')

    def input_user_telephone(self, telephone):
        self.send_keys(self.user_telephone_loc, telephone)

    submit_loc = ('xpath', '//*[@id="addHtml"]/p[4]/button')

    def click_submit(self):
        self.click(self.submit_loc)