from common.basics import Crazy

class LabelManagementPage(Crazy):
    '''标签管理'''
    configration_management_loc = ('xpath','//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[7]/div/span')

    def click_configration_management(self):
        self.click(self.configration_management_loc)

    label_management_loc = ('xpath','//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li[1]')

    def cliak_label_management(self):
        self.click(self.label_management_loc)

    search_label_name = ('xpath','//*[@id="tag"]')

    def input_search_label_name(self):
        self.send_keys(self.search_label_name,'塑')

    icon_search_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[1]/span/span/i')

    def click_icon_search(self):
        self.click(self.icon_search_loc)

    btn_search_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[1]')

    def click_btn_search(self):
        self.click(self.btn_search_loc)

    new_label_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[2]')

    def click_new_label(self):
        self.click(self.new_label_loc)

    spinner_label_type_loc = ('xpath','//form[@class="ant-form ant-form-horizontal"]/div/div[2]')

    def click_spinner_label_type(self):
        self.click(self.spinner_label_type_loc)

    newlabel_label_name_lco = ('xpath','//form[@class="ant-form ant-form-horizontal"]/div[2]/div[2]/div/span/input')

    def input_newlabel_label_name(self):
        self.send_keys(self.newlabel_label_name_lco,'测试标签')

    cancel_btn_loc = ('xpath', '//div[@class="ant-modal-footer"]/div/button[1]')

    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    determine_btn_lco = ('xpath', '//div[@class="ant-modal-footer"]/div/button[2]')

    def click_determine_btn(self):
        self.click(self.determine_btn_lco)

    operating_label_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/button')

    modify_label_loc = ('xpath','//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')

    def move_click_modify_label(self):
        self.move(self.operating_label_loc,self.modify_label_loc)

    delete_label_loc = ('xpath','//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')

    def move_click_delete_label(self):
        self.move(self.operating_label_loc, self.delete_label_loc)

    edit_spinner_label_type_loc = ('xpath','//form[@class="ant-form ant-form-horizontal"]/div/div[2]')

    def click_edit_spinner_label_type(self):
        self.click(self.edit_spinner_label_type_loc)

    dialog_cancel_loc = ('xpath','//div[@class="ant-confirm-btns"]/button[1]')

    def click_dialog_cancel(self):
        self.click(self.dialog_cancel_loc)