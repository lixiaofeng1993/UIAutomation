from common.basics import Crazy


class AccountManagementPage(Crazy):
    '''账号管理'''

    permission_manager_loc = ('xpath', '//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[10]/div')

    def click_permission_manager(self):
        self.click(self.permission_manager_loc)

    account_management_loc = ('xpath', '//*[@id="45$Menu"]/li[2]')

    def click_account_management(self):
        self.click(self.account_management_loc)

    add_account_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div/div/div/button')

    def click_add_account_btn(self):
        self.click(self.add_account_loc)

    addaccount_username_loc = ('xpath', '//*[@id="username"]')

    def input_addacc_username(self):
        self.send_keys(self.addaccount_username_loc, 'Test')

    addaccount_password_loc = ('xpath', '//*[@id="password"]')

    def input_addacc_password(self):
        self.send_keys(self.addaccount_password_loc, '123456')

    addaccount_name_loc = ('xpath', '//*[@id="name"]')

    def input_addacc_name(self):
        self.send_keys(self.addaccount_name_loc, '测试')

    addaccount_phone_loc = ('xpath', '//*[@id="phone"]')

    def input_addacc_phone(self):
        self.send_keys(self.addaccount_phone_loc, '13666668888')

    addaccount_remark_loc = ('xpath', '//*[@id="remark"]')

    def input_addacc_remark(self):
        self.send_keys(self.addaccount_remark_loc, '这是一个备注')

    addaccount_role_loc = (
    'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/span/div/div')

    def select_addacc_role(self):
        self.click(self.addaccount_role_loc)

    addaccount_cancel_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_addaccount_cancel(self):
        self.click(self.addaccount_cancel_loc)

    addaccount_detemine_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_addaccount_detemine(self):
        self.click(self.addaccount_detemine_loc)

    enable_disable_account_loc = (
    'xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[8]/div/button[2]')

    def click_enable_disable_account_btn(self):
        self.click(self.enable_disable_account_loc)

    dialog_isEnable_Disable_Cancel_loc = ('xpath', '/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[1]')

    def click_isEnable_Disable_Cancel_btn(self):
        self.click(self.dialog_isEnable_Disable_Cancel_loc)

    dialog_isEnable_Disable_Detemine_loc = (
    'xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button[2]')

    def click_isEnable_Disable_Detemine_btn(self):
        self.click(self.dialog_isEnable_Disable_Detemine_loc)

    edit_account_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[8]/div/button[1]')

    def click_edit_account_btn(self):
        self.click(self.edit_account_loc)

    dialog_editacc_name_loc = ('xpath', '//*[@id="name"]')

    def input_dialog_editacc_name(self):
        self.send_keys(self.dialog_editacc_name_loc, '测试部门人员')

    dialog_editacc_phone_loc = ('xpath', '//*[@id="phone"]')

    def input_dialog_editacc_phone(self):
        self.send_keys(self.dialog_editacc_phone_loc, '123456789')

    dialog_editacc_remark_loc = ('xpath', '//*[@id="remark"]')

    def input_dialog_editacc_remark(self):
        self.send_keys(self.dialog_editacc_remark_loc,'测试部账号')

    dialog_editacc_selectrole_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/span/div/div')

    dialog_editacc_selectrole02_loc = ('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span')

    def click_dialog_editacc_selectrole(self):
        self.click(self.dialog_editacc_selectrole_loc)

    def click_dialog_editacc_selectrole02(self):
        self.click(self.dialog_editacc_selectrole02_loc)

    dialog_editacc_cancel_loc = ('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_dialog_editacc_cancel(self):
        self.click(self.dialog_editacc_cancel_loc)

    dialog_editacc_detemine_loc = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_dialog_editacc_detemine(self):
        self.click(self.dialog_editacc_detemine_loc)

    previous_page_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[2]/a')

    def click_previous_page(self):
        self.click(self.previous_page_loc)

    next_page_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[5]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    spinner_select_row_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[6]/div[1]/div/span')

    def click_spinner_select_row(self):
        self.click(self.spinner_select_row_loc)

    input_jumperpage_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[6]/div[2]/input')

    def input_jumper_page(self):
        self.send_keys(self.input_jumperpage_loc,'2')

    input_jumper_page02_loc = ('xpath','//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[5]/div[2]/input')

    def input_jumper_page02(self):
        self.send_keys(self.input_jumper_page02_loc, '2')
