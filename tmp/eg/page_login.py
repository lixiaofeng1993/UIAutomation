from common.basics import Crazy


class LoginPage(Crazy):
    """登录模块元素封装"""

    phone_loc = ('name', 'userPhone')

    def input_phone(self, phone):
        self.send_keys(self.phone_loc, phone)

    pass_loc = ('name', 'userPass')

    def input_pass(self, password):
        self.send_keys(self.pass_loc, password)

    login_btn_loc = ('xpath', '/html/body/div/div/form/div/input')

    def click_login_btn(self):
        self.click(self.login_btn_loc)

    check_login_loc = ('xpath', '/html/body/header/span[6]')

    def check_login(self):
        return self.get_text(self.check_login_loc)

    quit_btn_loc = ('xpath', '/html/body/header/span[7]/a')

    def click_quit_btn(self):
        self.click(self.quit_btn_loc)

    def text_quit(self):
        return self.get_text(self.quit_btn_loc)

    register_btn_loc = ('xpath', '/html/body/header/span[7]/a')

    def text_register(self):
        return self.get_text(self.register_btn_loc)

    login_title_loc = ('xpath', '/html/body/div/div/div/span')

    def text_login_title(self):
        return self.get_text(self.login_title_loc)