#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 13:06
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_child_login.py
# @Software: PyCharm
from common.basics import Crazy


class ChildLoginPage(Crazy):
    """登录功能"""

    # 用户名称
    user_loc = ('id', 'username')

    def input_user(self, user):
        self.send_keys(self.user_loc, user)

    # 密码
    password_loc = ('id', 'password')

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    # 登录按钮
    login_btn_loc = ('class name', 'ant-btn')

    def click_login_btn(self):
        self.click(self.login_btn_loc)

    # 验证登录
    check_login_loc = ('xpath', '//*[@id="mainContainer"]/div[1]/div[2]/ul/li/div/span')

    def text_check_login(self):
        return self.get_text(self.check_login_loc)

    # login_error /div/div/div/span
    login_error_loc = ('xpath', '/html/body/div[2]/div/span/div/div/div/span')

    def text_login_error(self):
        return self.get_text(self.login_error_loc)
