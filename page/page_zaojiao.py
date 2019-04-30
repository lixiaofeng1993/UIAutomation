#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:31
# @Author  : lixiaofeng
# @File    : page_zaojiao.py
# @Software: PyCharm
# @desc    :

from common.basics import Crazy


class Zaojiaopage(Crazy):
    """早教小程序"""

    zao_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cw" and @text="包妈优选"]')

    def click_zao(self):
        self.click(self.zao_btn_loc)

    def element_zao(self):
        return self.find_element(self.zao_btn_loc)

    find_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/d7b" and @text="发现"]')  # 发现按钮

    def click_find(self):
        self.click(self.find_loc)

    title_btn_loc = ('xpath', '//*[@resource-id="android:id/title" and @text="小程序"]')  # 发现页小程序按钮

    def click_title_btn(self):
        self.click(self.title_btn_loc)

    helper_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="小程序助手"]')  # 小程序助手

    def element_helper(self):
        return self.find_element(self.helper_loc)

    def click_helper(self):
        self.click(self.helper_loc)

    zaojiao_small_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="包妈优选"]')  # 包妈优选小程序

    def element_zaojiao_small_btn(self):
        return self.find_element(self.zaojiao_small_btn_loc)

    delete_small_btn_loc = ('xpath', '//*[contains(@text, "删除")]')  # 删除小程序按钮

    def click_delete_small_btn(self):
        self.click(self.delete_small_btn_loc)

    edition_btn_loc = ('xpath', '//*[contains(@text, "百宝福利Buy")]')

    def element_edition_btn(self):
        return self.find_element(self.edition_btn_loc)

    delete_small1_btn_loc = ('xpath', '//*[contains(@text, "拖动到此处删除")]')

    def element_delete_small1_btn(self):
        return self.find_element(self.delete_small1_btn_loc)

    version_btn_loc = ('xpath', '//*[contains(@text, "版本查看")]')  # 版本查看按钮

    def click_version_btn(self):
        self.click(self.version_btn_loc)

    experience_version_btn_loc = ('xpath', '//*[contains(@text, "1.1.498")]')  # 体验版

    def click_experience_version_btn(self):
        self.click(self.experience_version_btn_loc)

    audition_class_btn_loc = ('xpath', '//*[contains(@text, "0元领取7节试听课")]')  # 领取试听课

    def click_audition_class_btn(self):
        self.click(self.audition_class_btn_loc)

    month_btn_loc = ('xpath', '//*[contains(@text, "2018")]')  # 选择月份

    def click_mouth_btn(self):
        self.click(self.month_btn_loc)

    sure_btn_loc = ('xpath', '//*[contains(@text, "确定")]')  # 确定按钮

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    # class_info_loc = ('xpath', '//*[contains(@text, "课程介绍")]')  # 课程介绍
    class_info_loc = ('xpath', '//android.widget.FrameLayout/android.view.ViewGroup[0]')  # 课程介绍

    def class_info_btn(self):
        self.click(self.class_info_loc)

    attend_lectures_btn_loc = ('xpath', '//*[contains(@text, "立即听课")]')  # 立即听课

    def click_attend_lectures_btn(self):
        self.click(self.attend_lectures_btn_loc)

    class_btn_loc = ('xpath', '//*[contains(@text, "预备课 预备课")]')  # 预备课 预备课

    def element_class_btn(self):
        return self.find_element(self.class_btn_loc)

    get_to_know_btn_loc = ('xpath', '//*[contains(@text, "立即了解正式课 ")]')  # 立即了解正式课

    def click_get_to_know_btn(self):
        self.click(self.get_to_know_btn_loc)

    def element_get_to_know_btn(self):
        return self.find_element(self.get_to_know_btn_loc)

    sure_buy_btn_loc = ('xpath', '//*[contains(@text, "立即购买")]')  # 立即购买

    def click_sure_buy_btn(self):
        self.click(self.sure_buy_btn_loc)

    buy_password_loc = ('id', 'com.tencent.mm:id/cei')  # 输入支付密码

    def input_buy_password(self, paw):
        self.send_keys(self.buy_password_loc, paw)

    check_buy_money_loc = ('id', 'com.tencent.mm:id/dhz')  # 获取支付金额

    def text_buy_money(self):
        return self.get_text(self.check_buy_money_loc)

    success_btn_loc = ('id', 'com.tencent.mm:id/f1w')  # 完成按钮

    def click_success_btn(self):
        self.click(self.success_btn_loc)

    check_address_btn_loc = ('xpath', '//*[contains(@text, "收货地址：请选择地址")]')  # 选择收货地址

    def click_check_address_btn(self):
        self.click(self.check_address_btn_loc)

    def element_check_address_btn(self):
        return self.find_element(self.check_address_btn_loc)

    add_address_btn_loc = ('xpath', '//*[contains(@text, "添加地址")]')  # 添加地址

    def click_add_address_btn(self):
        self.click(self.add_address_btn_loc)

    name_loc = ('xpath', '//*[contains(@text, "请输入你的姓名")]')  # 请输入你的姓名

    def input_name_btn(self, name):
        self.send_keys(self.name_loc, name)

    phone_btn_loc = ('xpath', '//*[contains(@text, "请填写收件人电话")]')  # 请填写收件人电话

    def input_phone_btn(self, phone):
        self.send_keys(self.phone_btn_loc, phone)

    region_btn_loc = ('xpath', '//*[contains(@text, "请输入你所在地区")]')  # 请输入你所在地区

    def click_region_btn(self):
        self.click(self.region_btn_loc)

    detailed_address_btn_loc = ('xpath', '//*[contains(@text, "请输入你的详细地址")]')  # 请输入你的详细地址

    def input_detailed_address_btn(self, address):
        self.send_keys(self.detailed_address_btn_loc, address)

    save_btn_loc = ('xpath', '//*[contains(@text, "保存")]')  # 保存

    def click_save_btn(self):
        self.click(self.save_btn_loc)

    receive_btn_loc = ('xpath', '//*[contains(@text, "立即领取")]')  # 立即领取

    def click_receive_btn(self):
        self.click(self.receive_btn_loc)

    addressee_loc = ('xpath', '//*[contains(@text, "收件人：")]')  # 地址列表是否有地址信息

    def elements_addressee(self):
        return self.find_elements(self.addressee_loc)

    def clicks_addressee(self):
        self.clicks(self.addressee_loc, 0)

    know_btn_loc = ('xpath', '//*[contains(@text, "知道了")]')  # 地址列表是否有地址信息

    def element_know(self):
        return self.find_element(self.know_btn_loc)

    def click_know(self):
        self.click(self.know_btn_loc)

    all_curriculum_btn_loc = ('xpath', '//*[contains(@text, "查看全部课程")]')  # 查看全部课程

    def element_all_curriculum_btn(self):
        return self.find_element(self.all_curriculum_btn_loc)

    def click_all_curriculum_btn(self):
        self.click(self.all_curriculum_btn_loc)

    curriculum_date_btn_loc = ('xpath', '//*[contains(@text, "2019-0")]')  # 历史推送

    def element_curriculum_date_btn(self):
        return self.find_element(self.curriculum_date_btn_loc)

    my_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cs" and @text="我的"]')  # 我的

    def element_my_btn(self):
        return self.find_element(self.my_btn_loc)

    def click_my(self):
        self.click(self.my_btn_loc)

    my_baby_btn_loc = ('xpath', '//*[contains(@text, "我的宝宝")]')  # 我的宝宝

    def click_my_baby(self):
        self.click(self.my_baby_btn_loc)

    my_baby_title_loc = ('id', 'com.tencent.mm:id/oa')

    def text_my_baby_title(self):
        return self.get_text(self.my_baby_title_loc)

    new_baby_btn_loc = ('xpath', '//*[contains(@text, "新建宝宝")]')  # 新建宝宝

    def element_new_baby_btn(self):
        return self.find_element(self.new_baby_btn_loc)

    def click_new_baby_btn(self):
        self.click(self.new_baby_btn_loc)

    next_btn_loc = ('xpath', '//*[contains(@text, "下一步")]')  # 我的宝宝

    def click_next(self):
        self.click(self.next_btn_loc)

    baby_name_loc = ('xpath', '//*[contains(@text, "请输入宝宝姓名")]')  # 请输入宝宝姓名

    def input_baby_name(self, name):
        self.send_keys(self.baby_name_loc, name)

    baby_bir_btn_loc = ('xpath', '//*[contains(@text, "宝宝的生日:")]')  # 宝宝的生日

    def click_baby_bir_btn(self):
        self.click(self.baby_bir_btn_loc)

    finish_btn_loc = ('xpath', '//*[contains(@text, "完成")]')  # 完成按钮

    def click_finish_btn(self):
        self.click(self.finish_btn_loc)

    my_home_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cs" and @text="首页"]')  # 首页

    def click_my_home(self):
        self.click(self.my_home_loc)

    def element_my_home(self):
        return self.find_element(self.my_home_loc)

    switch_btn_loc = ('xpath', '//*[contains(@text, "切换")]')  # 切换

    def click_switch_btn(self):
        self.click(self.switch_btn_loc)

    baby_bri_loc = ('xpath', '//*[contains(@text, "宝宝生日：")]')  # 宝宝生日：

    def click_baby_bri(self):
        self.click(self.baby_bri_loc)

    class_img_btn_loc = ('xpath', 'android.widget.Image')

    def clicks_class_img(self):
        self.clicks(self.class_img_btn_loc, 0)

    collection_btn_loc = ('xpath', '//*[contains(@text, "收藏")]')  # 收藏

    def click_collection_btn(self):
        self.click(self.collection_btn_loc)

    write_record_btn_loc = ('xpath', '//*[contains(@text, "写记录")]')  # 写记录按钮

    def click_write_record_btn(self):
        self.click(self.write_record_btn_loc)

    album_btn_loc = ('xpath', '//*[contains(@text, "相册")]')  # 相册

    def click_album_btn(self):
        self.click(self.album_btn_loc)

    small_video_btn_loc = ('xpath', '//*[contains(@text, "小视频")]')  # 小视频

    def click_small_video_btn(self):
        self.click(self.small_video_btn_loc)

    release_btn_loc = ('xpath', '//*[contains(@text, "发布")]')  # 发布

    def click_release_btn(self):
        self.click(self.release_btn_loc)

    class_name_loc = ('xpath', '//*[contains(@text, "测试英语课程组")]')  # 课程名称

    def click_class_name(self):
        self.click(self.class_name_loc)

    class_name2_loc = ('xpath', '//*[contains(@text, "测试游戏课程")]')  # 课程名称

    def click_class2_name(self):
        self.click(self.class_name2_loc)

    write_text_loc = ('xpath', '//*[contains(@text, "0/256")]')  # 写记录

    def input_write_text(self, text):
        self.send_keys(self.write_text_loc, text)

    choice_album_loc = ('id', 'com.tencent.mm:id/bot')

    def clicks_choice_album(self, n):
        self.clicks(self.choice_album_loc, n)

    complete_btn_loc = ('id', 'com.tencent.mm:id/jx')  # 完成

    def click_complete_btn(self):
        self.click(self.complete_btn_loc)

    my_collection_btn_loc = ('xpath', '//*[contains(@text, "我的收藏")]')  # 我的收藏

    def click_my_collection_btn(self):
        self.click(self.my_collection_btn_loc)

    my_collection_english_course_btn_loc = ('xpath', '//*[contains(@text, "早教")]')  # 早教英语课

    def elements_my_collection_english_course_btn(self):
        return self.find_elements(self.my_collection_english_course_btn_loc)

    my_course_btn_loc = ('xpath', '//*[contains(@text, "我的课程")]')  # 我的课程

    def click_my_course_btn(self):
        self.click(self.my_course_btn_loc)

    my_course_buy_btn_loc = ('xpath', '//*[contains(@text, "早教核心课半年卡")]')  # 早教核心课半年卡

    def elements_my_course_buy_btn(self):
        return self.find_elements(self.my_course_buy_btn_loc)

    my_order_btn_loc = ('xpath', '//*[contains(@text, "我的订单")]')  # 我的订单

    def click_my_order_btn(self):
        self.click(self.my_order_btn_loc)

    my_order_card_btn_loc = ('xpath', '//*[contains(@text, "订单编号：")]')  # 订单编号：

    def elements_my_order_card_btn(self):
        return self.find_elements(self.my_order_card_btn_loc)

    my_record_btn_loc = ('xpath', '//*[contains(@text, "成长记录")]')  # 成长记录

    def click_my_record_btn(self):
        self.click(self.my_record_btn_loc)

    my_record_class_btn_loc = ('xpath', '//*[contains(@text, "#")]')  # # 测试英语课程组

    def elements_my_record_class_btn(self):
        return self.find_elements(self.my_record_class_btn_loc)

    back_btn_loc = (
        'xpath', '//*[@resource-id="com.tencent.mm:id/o3" and @class="android.widget.LinearLayout"]')  # 返回按钮

    def element_back_btn(self):
        return self.find_element(self.back_btn_loc)

    def click_back_btn(self):
        self.click(self.back_btn_loc)

    reply_5_loc = ('xpath', '//android.widget.Image')  # 回复5

    def click_reply_5(self):
        self.click(self.reply_5_loc)

    add_to_btn_loc = ('xpath', '//*[contains(@text, "立即添加")]')  # 立即添加

    def click_add_to_btn(self):
        self.click(self.add_to_btn_loc)

    reply_input_5_loc = ('id', 'com.tencent.mm:id/amb')

    def input_reply_5(self, num):
        self.send_keys(self.reply_input_5_loc, num)

    send_5_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/ami" and @text="发送"]')  # 发送

    def click_send(self):
        self.click(self.send_5_loc)

    reply_code_loc = ('id', 'com.tencent.mm:id/aou')  # 获取回复的二维码

    def elements_reply_code(self):
        return self.find_elements(self.reply_code_loc)

    long_code_loc = ('id', 'com.tencent.mm:id/adf')  # 长按二维码

    def element_long_code(self):
        return self.find_element(self.long_code_loc)

    def click_long_code(self):
        self.click(self.long_code_loc)

    discern_code_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cw" and @text="识别图中二维码"]')  # 识别图中二维码

    def click_discern_code(self):
        self.click(self.discern_code_loc)

    class_group_loc = ('id', 'android:id/text1')  # 群名称

    def text_class_group(self):
        return self.get_text(self.class_group_loc)

    reply_8_loc = ('xpath', '//android.widget.Image')  # 回复8的banner     回复8->进公众号->点击推送 看到的二维码

    def elements_reply_8(self):
        return self.find_elements(self.reply_8_loc)

    parent_btn_loc = ('xpath', '//*[contains(@text, "亲爱的家长：")]')  # 亲爱的家长：

    def element_parent_btn(self):
        return self.find_element(self.parent_btn_loc)

    info_btn_loc = ('id', 'com.tencent.mm:id/a7n')

    def elements_info_btn(self):
        return self.find_elements(self.info_btn_loc)

    more_games_btn_loc = ('xpath', '//*[contains(@text, "更多亲子游戏")]')  # 更多亲子游戏

    def click_more_games_btn(self):
        self.click(self.more_games_btn_loc)

    look_all_btn_loc = ('xpath', '//*[contains(@text, "查看全部")]')  # 查看全部

    def click_look_all_btn(self):
        self.click(self.look_all_btn_loc)
