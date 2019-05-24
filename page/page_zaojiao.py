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

    zao_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cx" and @text="包妈优选"]')

    # zao_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cx" and @text="小小包早教"]')

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

    small_help_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cx" and @text="小程序助手"]')  # 小程序助手

    def click_small_help_btn(self):
        self.click(self.small_help_btn_loc)

    small_name_loc = ('xpath', '//*[contains(@text, "包妈优选")]')  # 包妈优选

    def element_small_name(self):
        return self.find_element(self.small_name_loc)

    def click_small_name(self):
        self.click(self.small_name_loc)

    switching_applet_btn_loc = ('xpath', '//*[contains(@text, "切换小程序")]')  # 切换小程序

    def click_switching_applet_btn(self):
        self.click(self.switching_applet_btn_loc)

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

    experience_version_btn_loc = ('xpath', '//*[contains(@text, "6.0.04")]')  # 体验版

    def clicks_experience_version_btn(self):
        self.clicks(self.experience_version_btn_loc, -1)

    audition_class_btn_loc = ('xpath', '//*[contains(@text, "0元领取7节试听课")]')  # 领取试听课

    def element_audition_class_btn(self):
        return self.find_element(self.audition_class_btn_loc)

    def click_audition_class_btn(self):
        self.click(self.audition_class_btn_loc)

    wechat_grant_btn_loc = (('xpath', '//*[contains(@text, "微信授权") and @class="android.widget.Button" ]'))  # 微信授权

    def click_wechat_grant_btn(self):
        self.click(self.wechat_grant_btn_loc)

    def double_click_wechat_grant(self):
        self.double_click(self.wechat_grant_btn_loc)

    def element_wechat_grant_btn(self):
        return self.find_element(self.wechat_grant_btn_loc)

    allow_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/st" and @text="允许"]')  # 完成按钮

    def click_allow_btn(self):
        self.click(self.allow_btn_loc)

    month_btn_loc = ('xpath', '//*[contains(@text, "2018")]')  # 选择月份

    def click_mouth_btn(self):
        self.click(self.month_btn_loc)

    sure_btn_loc = ('xpath', '//*[contains(@text, "确定")]')  # 确定按钮

    def click_sure_btn(self):
        self.click(self.sure_btn_loc)

    class_info_loc = ('xpath', '//*[contains(@text, "课程介绍")]')  # 课程介绍
    # class_info_loc = ('xpath', '//android.widget.FrameLayout/android.view.ViewGroup[0]')  # 课程介绍

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

    buy_password_loc = ('id', 'com.tencent.mm:id/cfs')  # 输入支付密码

    def input_buy_password(self, paw):
        self.send_keys(self.buy_password_loc, paw)

    check_buy_money_loc = ('id', 'com.tencent.mm:id/dlh')  # 获取支付金额

    def text_buy_money(self):
        return self.get_text(self.check_buy_money_loc)

    success_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/f8o" and @text="完成"]')  # 完成按钮

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

    my_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/ct" and @text="我的"]')  # 我的

    def element_my_btn(self):
        return self.find_element(self.my_btn_loc)

    def click_my(self):
        self.click(self.my_btn_loc)

    my_baby_btn_loc = ('xpath', '//*[contains(@text, "我的宝宝")]')  # 我的宝宝

    def click_my_baby(self):
        self.click(self.my_baby_btn_loc)

    my_baby_title_loc = ('id', 'com.tencent.mm:id/ox')

    def text_my_baby_title(self):
        return self.get_text(self.my_baby_title_loc)

    def elements_title(self):
        return self.find_elements(self.my_baby_title_loc)

    new_baby_btn_loc = ('xpath', '//*[contains(@text, "新建宝宝")]')  # 新建宝宝

    def element_new_baby_btn(self):
        return self.find_element(self.new_baby_btn_loc)

    def click_new_baby_btn(self):
        self.click(self.new_baby_btn_loc)

    def clicks_new_baby_btn(self, n):
        self.clicks(self.new_baby_btn_loc, n)

    get_set_loc = ('xpath', '//*[contains(@text, "预备课 预备课")]')  # 新建宝宝

    def element_get_set(self):
        return self.find_element(self.get_set_loc)

    next_btn_loc = ('xpath', '//*[contains(@text, "下一步")]')  # 我的宝宝

    def click_next(self):
        self.click(self.next_btn_loc)

    baby_name_loc = ('xpath', '//*[contains(@text, "请输入宝宝姓名")]')  # 请输入宝宝姓名

    def inputs_baby_name(self, name, n):
        self.sends_keys(self.baby_name_loc, name, n)

    baby_bir_btn_loc = ('xpath', '//*[contains(@text, "宝宝的生日:")]')  # 宝宝的生日

    def click_baby_bir_btn(self):
        self.click(self.baby_bir_btn_loc)

    finish_btn_loc = ('xpath', '//*[contains(@text, "完成")]')  # 完成按钮

    def click_finish_btn(self):
        self.click(self.finish_btn_loc)

    def clicks_finish_btn(self, n):
        self.clicks(self.finish_btn_loc, n)

    my_home_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/ct" and @text="首页"]')  # 首页

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

    def clicks_collection_btn(self, n):
        self.clicks(self.collection_btn_loc, n)

    def element_collection_btn(self):
        return self.find_element(self.collection_btn_loc)

    write_record_btn_loc = ('xpath', '//*[contains(@text, "写记录") and @class="android.widget.Button" ]')  # 写记录按钮

    def click_write_record_btn(self):
        self.click(self.write_record_btn_loc)

    def clicks_write_record_btn(self, n):
        self.clicks(self.write_record_btn_loc, n)

    album_btn_loc = ('xpath', '//*[contains(@text, "相册")]')  # 相册

    def click_album_btn(self):
        self.click(self.album_btn_loc)

    def element_album_btn(self):
        return self.find_element(self.album_btn_loc)

    small_video_btn_loc = ('xpath', '//*[contains(@text, "小视频")]')  # 小视频

    def click_small_video_btn(self):
        self.click(self.small_video_btn_loc)

    def element_small_video_btn(self):
        return self.find_element(self.small_video_btn_loc)

    release_btn_loc = ('xpath', '//*[contains(@text, "发布")]')  # 发布

    def click_release_btn(self):
        self.click(self.release_btn_loc)

    def clicks_release_btn(self, n):
        self.clicks(self.release_btn_loc, n)

    def element_record_info(self, data):  # 判断是否定位到包含text的元素
        record_info_loc = ('xpath', '//*[contains(@text, "{}")]'.format(data))
        record_info = self.find_element(record_info_loc)
        if record_info:
            return True
        else:
            return False

    class_name_loc = ('xpath', '//*[contains(@text, "测试英语课程组")]')  # 课程名称

    # class_name_loc = ('xpath', '//*[contains(@text, "歌曲：Head and shoulders")]')  # 课程名称

    def click_class_name(self):
        self.click(self.class_name_loc)

    def clicks_class_name(self, n):
        self.clicks(self.class_name_loc, n)

    def elements_class_name(self):
        return self.find_elements(self.class_name_loc)

    class_name2_loc = ('xpath', '//*[contains(@text, "测试游戏课程")]')  # 课程名称

    # class_name2_loc = ('xpath', '//*[contains(@text, "弹出来的画")]')  # 课程名称

    def click_class2_name(self):
        self.click(self.class_name2_loc)

    def clicks_class2_name(self, n):
        self.clicks(self.class_name2_loc, n)

    write_text_loc = ('xpath', '//*[contains(@text, "0/1000")]')  # 写记录

    def input_write_text(self, text):
        self.send_keys(self.write_text_loc, text)

    def inputs_write_text(self, text, n):
        self.sends_keys(self.write_text_loc, text, n)

    choice_album_loc = ('id', 'com.tencent.mm:id/bpy')

    def clicks_choice_album(self, n):
        self.clicks(self.choice_album_loc, n)

    def elements_choice_album(self):
        return self.find_elements(self.choice_album_loc)

    complete_btn_loc = ('id', 'com.tencent.mm:id/ki')  # 完成

    def click_complete_btn(self):
        self.click(self.complete_btn_loc)

    my_collection_btn_loc = ('xpath', '//*[contains(@text, "我的收藏")]')  # 我的收藏

    def click_my_collection_btn(self):
        self.click(self.my_collection_btn_loc)

    my_collection_english_course_btn_loc = ('xpath', '//*[contains(@text, "早教")]')  # 早教英语课

    def elements_my_collection_english_course_btn(self):
        return self.find_elements(self.my_collection_english_course_btn_loc)

    my_collection_game_course_btn_loc = ('xpath', '//*[contains(@text, "宝宝游戏馆")]')  # 宝宝游戏馆

    def elements_my_collection_game_course_btn(self):
        return self.find_elements(self.my_collection_game_course_btn_loc)

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
        'xpath', '//*[@resource-id="com.tencent.mm:id/on" and @class="android.widget.LinearLayout"]')  # 返回按钮

    def element_back_btn(self):
        return self.find_element(self.back_btn_loc)

    def click_back_btn(self):
        self.click(self.back_btn_loc)

    reply_5_loc = ('xpath', '//android.widget.Image')  # 回复5

    def click_reply_5(self):
        self.click(self.reply_5_loc)

    def elements_reply_5(self):
        return self.find_elements(self.reply_5_loc)

    add_to_btn_loc = ('xpath', '//*[contains(@text, "立即添加")]')  # 立即添加

    def click_add_to_btn(self):
        self.click(self.add_to_btn_loc)

    reply_input_5_loc = ('id', 'com.tencent.mm:id/ami')

    def input_reply_5(self, num):
        self.send_keys(self.reply_input_5_loc, num)

    send_5_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/amp" and @text="发送"]')  # 发送

    def click_send(self):
        self.click(self.send_5_loc)

    reply_code_loc = ('id', 'com.tencent.mm:id/ap9')  # 获取回复的二维码

    def elements_reply_code(self):
        return self.find_elements(self.reply_code_loc)

    def clicks_reply_code(self, n):
        self.clicks(self.reply_code_loc, n)

    long_code_loc = ('id', 'com.tencent.mm:id/adi')  # 长按二维码

    def element_long_code(self):
        return self.find_element(self.long_code_loc)

    def click_long_code(self):
        self.click(self.long_code_loc)

    discern_code_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cx" and @text="识别图中二维码"]')  # 识别图中二维码

    def click_discern_code(self):
        self.click(self.discern_code_loc)

    class_group_loc = ('id', 'android:id/text1')  # 群名称

    def text_class_group(self):
        return self.get_text(self.class_group_loc)

    add_group_chat_loc = ('xpath', '//*[contains(@text, "加入该群聊")]')  # 加入该群聊

    def element_add_group_chat(self):
        return self.find_element(self.add_group_chat_loc)

    reply_8_loc = ('xpath', '//android.widget.Image')  # 回复8的banner     回复8->进公众号->点击推送 看到的二维码

    def elements_reply_8(self):
        return self.find_elements(self.reply_8_loc)

    parent_btn_loc = ('xpath', '//*[contains(@text, "亲爱的家长：")]')  # 亲爱的家长：

    def element_parent_btn(self):
        return self.find_element(self.parent_btn_loc)

    info_btn_loc = ('id', 'com.tencent.mm:id/a8q')  # 详情

    def elements_info_btn(self):
        return self.find_elements(self.info_btn_loc)

    def clicks_info_btn(self, n):
        self.clicks(self.info_btn_loc, n)

    more_games_btn_loc = ('xpath', '//*[contains(@text, "更多亲子游戏")]')  # 更多亲子游戏

    def click_more_games_btn(self):
        self.click(self.more_games_btn_loc)

    look_all_btn_loc = ('xpath', '//*[contains(@text, "查看全部")]')  # 查看全部

    def click_look_all_btn(self):
        self.click(self.look_all_btn_loc)

    def element_look_all_btn(self):
        return self.find_elements(self.look_all_btn_loc)

    start_fingerprint_buy_loc = ('id', 'com.tencent.mm:id/btp')  # 开启指纹支付弹窗文本   开启指纹支付，支付时可通过验证指纹快速完成付款。

    def text_start_fingerprint_buy(self):
        return self.get_text(self.start_fingerprint_buy_loc)

    no_more_reminder_btn_loc = ('id', 'com.tencent.mm:id/btq')  # 不再提醒

    def click_no_more_reminder_btn(self):
        self.click(self.no_more_reminder_btn_loc)

    cancel_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/azz" and @text="取消"]')  # 取消

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    usd_password_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/fg4" and @text="使用密码"]')  # 使用密码

    def element_usd_password(self):
        return self.find_element(self.usd_password_loc)

    def click_usd_password(self):
        self.click(self.usd_password_loc)

    password_error_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/d8x" and @text="支付密码错误，请重试"]')  # 支付密码错误，请重试

    def element_password_error(self):
        return self.find_element(self.password_error_loc)

    again_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/azz" and @text="重试"]')  # 重试

    def click_again_btn(self):
        self.click(self.again_btn_loc)

    payment_loc = ('id', 'com.tencent.mm:id/fg3')  # 请输入支付密码 文本

    def text_payment(self):
        return self.get_text(self.payment_loc)

    typewriting_finish_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/z2" and @text="完成"]')  # 输入法上的完成按钮

    def element_typewriting_finish_btn(self):
        return self.find_element(self.typewriting_finish_btn_loc)

    def click_typewriting_finish_btn(self):
        self.click(self.typewriting_finish_btn_loc)

    # 打卡

    clock_btn_loc = ('xpath', '//*[contains(@text, "打卡")]')  # 打卡

    def click_clock_btn(self):
        self.click(self.clock_btn_loc)

    def element_clock_btn(self):
        return self.find_element(self.clock_btn_loc)

    # com.tencent.mm:id/ox

    no_clock_btn_loc = ('xpath', '//*[contains(@text, "你还未开启打卡")]')  # 你还未开启打卡

    def element_no_clock_btn(self):
        return self.find_element(self.no_clock_btn_loc)

    get_card_btn_loc = ('xpath', '//*[@text="获取打卡海报" and @class="android.widget.Button"]')  # 获取打卡海报

    def click_get_card_btn(self):
        self.click(self.get_card_btn_loc)

    upload_card_btn_loc = ('xpath', '//*[@text="上传截图" and @class="android.widget.Button"]')  # 上传截图

    def click_upload_card_btn(self):
        self.click(self.upload_card_btn_loc)

    again_upload_card_btn_loc = ('xpath', '//*[@text="重新上传截图" and @class="android.widget.Button"]')  # 重新上传截图

    def click_again_upload_card_btn(self):
        self.click(self.again_upload_card_btn_loc)

    save_img_btn_loc = ('xpath', '//*[@text="保存图片" and @class="android.widget.Button"]')  # 保存图片

    def click_save_img_btn(self):
        self.click(self.save_img_btn_loc)

    copy_text_btn_loc = ('xpath', '//*[@text="复制发圈文案" and @class="android.widget.Button"]')  # 复制发圈文案

    def click_copy_text_btn(self):
        self.click(self.copy_text_btn_loc)

    copy_format_btn_loc = ('xpath', '//*[contains(@text, "发布朋友圈截图规范")]')  # 发布朋友圈截图规范

    def element_copy_format_btn(self):
        return self.find_element(self.copy_format_btn_loc)

    card_go_btn_loc = ('xpath', '//*[contains(@text, "关闭小程序，去朋友圈打卡截图")]')  # 关闭小程序，去朋友圈打卡截图

    def click_card_go_btn(self):
        self.click(self.card_go_btn_loc)

    upload_btn_loc = ('xpath', '//*[@text="上传" and @class="android.widget.Button"]')  # 上传

    def click_upload_btn(self):
        self.click(self.upload_btn_loc)

    today_card_btn_loc = ('xpath', '//*[contains(@text, "今日已提交打卡")]')  # 今日已提交打卡

    def element_today_card_btn(self):
        return self.find_element(self.today_card_btn_loc)

    reset_img_btn_loc = ('xpath', '//*[@text="重新选择截图" and @class="android.widget.Button"]')  # 重新选择截图

    def click_reset_img_btn(self):
        self.click(self.reset_img_btn_loc)

    generated_loading_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cx" and @text="正在生成..."]')  # 正在生成...

    def element_generated_loading(self):
        return self.find_element(self.generated_loading_loc)

    reminder_btn_loc = ('xpath', '//*[contains(@text, "温馨提示")]')  # 温馨提示

    def element_reminder_btn(self):
        return self.find_element(self.reminder_btn_loc)

    page_expired_loc = ('xpath', '//*[contains(@text, "页面已经过期")]')  # 页面已经过期

    def element_page_expired(self):
        return self.find_element(self.page_expired_loc)

    x_btn_loc = ('id', 'com.tencent.mm:id/kx')

    def click_x_btn(self):
        self.click(self.x_btn_loc)
