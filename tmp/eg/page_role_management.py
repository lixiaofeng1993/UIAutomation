# coding:utf-8
from common.basics import Crazy


class RoleManagementPage(Crazy):
    '''角色管理'''

    permission_manager_loc = ('xpath', '//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[10]/div')

    def click_permission_manager(self):
        self.click(self.permission_manager_loc)

    role_management_loc = ('xpath', '//*[@id="45$Menu"]/li[1]')

    def click_role_management(self):
        self.click(self.role_management_loc)

    role_input_loc = ('xpath', '//*[@id="queryString"]')

    def input_role_text(self):
        self.send_keys(self.role_input_loc, '测试部')

    icon_search_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[1]/span/span/i')

    def click_icon_search(self):
        self.click(self.icon_search_loc)

    button_search_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[1]')

    def click_button_search(self):
        self.click(self.button_search_loc)

    btn_addrole_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[2]')

    def click_btn_addrole(self):
        self.click(self.btn_addrole_loc)

    diaolog_addrole_text_loc = ('xpath', '//*[@id="name"]')

    def input_dialog_addrole(self):
        self.send_keys(self.diaolog_addrole_text_loc, 'Test_add_role')

    checkBox_add_permissionConfiguration_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div/label[2]/span[1]')

    def click_checkBox_add_permissionConfig(self):
        self.click(self.checkBox_add_permissionConfiguration_loc)

    dialog_add_rolename_cancel_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_dialog_addRoleName_cancel(self):
        self.click(self.dialog_add_rolename_cancel_loc)

    dialog_add_rolename_detemine_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_dialog_addRoleName_detemine(self):
        self.click(self.dialog_add_rolename_detemine_loc)

    # 设置权限
    button_set_permission_loc = (
        'xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[8]/td[3]/div/button')

    def click_btn_set_permission(self):
        self.click(self.button_set_permission_loc)

    dialog_input_rolename_loc = ('xpath', '//*[@id="name"]')

    def input_dialogInput_rolename(self):
        self.send_keys(self.dialog_input_rolename_loc, '测试一部')

    checkBox_permissionConfiguration_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div/label[6]/span[1]')

    def click_checkbox_permissionConfiguration(self):
        self.click(self.checkBox_permissionConfiguration_loc)

    dialog_permissionConfiguration_cancel_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_dialog_permissionconfig_cancel(self):
        self.click(self.dialog_permissionConfiguration_cancel_loc)

    dialog_permissionConfiguration_determine_loc = (
        'xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_dialog_permissionconfig_determine(self):
        self.click(self.dialog_permissionConfiguration_determine_loc)

    icon_previouspage_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[2]/a')

    def click_icon_previouspage(self):
        self.click(self.icon_previouspage_loc)

    icon_nextpage_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[4]/a')

    def click_icon_nextpage(self):
        self.click(self.icon_nextpage_loc)

    spinner_select_row_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[5]/div[1]/div/span')

    def click_spinner_selectrow(self):
        self.click(self.spinner_select_row_loc)
        self.send_keys_arrow_down()

    input_jumperpages_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[5]/div[2]/input')

    def input_jumperpages(self):
        self.send_keys(self.input_jumperpages_loc,2)
