from common.basics import Crazy


class CarLoginPage(Crazy):
    """元素定位，登录功能"""

    # 跳过广告
    skip_loc = ('id', 'com.ss.android.auto:id/c8r')

    def click_skip(self):
        self.click(self.skip_loc)

    tag_loc = ("id", "com.ss.android.auto:id/bqp")

    # 首页文本
    def text_home(self):
        return self.get_texts(self.tag_loc, 0)

    # 是否未 登录
    def text_landed(self):
        return self.get_texts(self.tag_loc, 3)

    # 进入 未登录(我的)页面
    def click_landed(self):
        self.clicks(self.tag_loc, 3)

    # # 判断是否进入未登录(我的)页  设置  编辑资料
    common_loc = ('id', 'com.ss.android.auto:id/dd')

    def text_common(self):
        return self.get_text(self.common_loc)

    # 点击手机图标
    phone_loc = ('id', 'com.ss.android.auto:id/brg')

    def click_phone(self):
        self.click(self.phone_loc)

    # 判断是否进入手机登录页面
    phone_login_loc = ('id', 'com.ss.android.auto:id/jv')

    def text_phone_login(self):
        return self.get_text(self.phone_login_loc)

    # 输入手机号
    _phone_loc = ('id', 'com.ss.android.auto:id/jy')

    def input_phone(self, phone):
        self.send_keys(self._phone_loc, phone)

    # 点击获取验证码
    verification_code_loc = ('id', 'com.ss.android.auto:id/jz')

    def click_verification_code(self):
        self.click(self.verification_code_loc)

    # 输入验证码
    input_verification_code_loc = ('id', 'com.ss.android.auto:id/k3')

    def input_verification(self, code):
        self.send_keys(self.input_verification_code_loc, code)

    # 点击 进入app 按钮
    into_btn_loc = ('id', 'com.ss.android.auto:id/k7')

    def click_into_btn(self):
        self.click(self.into_btn_loc)

    # QQ登录
    qq_loc = ('id', 'com.ss.android.auto:id/brh')

    def click_qq(self):
        self.click(self.qq_loc)

    # 授权按钮
    # grant_btn_loc = ('id', 'com.tencent.mobileqq:id/name') [36,1418][1044,1538]
    # grant_btn_loc = [(36, 1301), (1044, 1421)]
    grant_btn_loc = [(36, 1418), (1044, 1538)]

    def click_grant_btn(self):
        self.click_coordinate(self.grant_btn_loc)

    # 判断登录成功
    personal_center_loc = ('id', 'com.ss.android.auto:id/br3')

    def text_personal_center(self):
        return self.get_text(self.personal_center_loc)

    # 微信登录
    wechat_loc = ('id', 'com.ss.android.auto:id/bri')

    def click_wechat(self):
        self.click(self.wechat_loc)

    # 确认登录 [42,1176][1038,1320] com.tencent.mm:id/ch6  [39,1079][1041,1211] [42,1176][1038,1320]
    confirm_wechat_loc = [(42, 1176), (1038, 1320)]

    def click_confirm_wechat(self):
        self.click_coordinate(self.confirm_wechat_loc)

    # 退出操作
    set_up_loc = ('id', 'com.ss.android.auto:id/bvb')

    def click_set_up(self):
        self.click(self.set_up_loc)

    # 判断进入设置页 text_common

    # 退出按钮
    logout_loc = ('id', 'com.ss.android.auto:id/c7o')

    def click_logout(self):
        self.click(self.logout_loc)

    # 是否存在退出按钮
    def element_logout(self):
        return self.find_element(self.logout_loc)

    # 退出确认
    logout_confirm_loc = ('id', 'com.ss.android.auto:id/i3')

    def text_logout_confirm(self):
        return self.get_text(self.logout_confirm_loc)

    # 确认退出
    confirm_logout_loc = ('id', 'com.ss.android.auto:id/c9_')

    def click_confirm_logout(self):
        self.click(self.confirm_logout_loc)

    # 修改资料
    update_user_loc = ('id', 'com.ss.android.auto:id/br5')

    def click_update_user(self):
        self.click(self.update_user_loc)

    # 用户名
    user_name_loc = ('id', 'com.ss.android.auto:id/j_')

    def click_user_name(self):
        self.click(self.user_name_loc)

    # 请输入用户名 title
    enter_user_loc = ('id', 'com.ss.android.auto:id/ali')

    def text_enter_user(self):
        return self.get_text(self.enter_user_loc)

    # 修改用户名
    input_user_loc = ('id', 'com.ss.android.auto:id/alj')

    def input_user(self, name):
        self.send_keys(self.input_user_loc, name)

    # 确定按钮
    enter_btn_loc = ('id', 'com.ss.android.auto:id/alm')

    def click_enter_btn(self):
        self.click(self.enter_btn_loc)

    # 获取用户名称
    get_user_name_loc = ('id', 'com.ss.android.auto:id/jc')

    def text_get_user_name(self):
        return self.get_text(self.get_user_name_loc)
