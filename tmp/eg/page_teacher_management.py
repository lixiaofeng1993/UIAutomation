from common.basics import Crazy


class TeacherManagementPage(Crazy):
    '''老师管理'''

    teacher_management_loc = ('xpath', '//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[8]/a')

    def click_teacher_management(self):
        self.click(self.teacher_management_loc)

    search_teacher_name_loc = ('xpath','//*[@id="queryString"]')

    def input_search_teachername(self):
        self.send_keys(self.search_teacher_name_loc,'小')

    query_btn_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[1]')

    def click_query_btn(self):
        self.click(self.query_btn_loc)

    add_teacher_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[2]/div/div/button[2]')

    def click_add_teacher(self):
        self.click(self.add_teacher_loc)

    add_teacher_name_loc = ('xpath','//*[@id="name"]')

    def input_add_teacher_name(self):
        self.send_keys(self.add_teacher_name_loc,'小老师')

    add_teacher_phone_loc = ('xpath','//*[@id="phone"]')

    def input_add_teacher_phone(self):
        self.send_keys(self.add_teacher_phone_loc,'13666668888')

    add_teacher_title_loc = ('xpath', '//*[@id="socialTitle"]')

    def input_add_teacher_title(self):
        self.send_keys(self.add_teacher_title_loc, '人民的园丁')

    select_sex_girl_loc = ('xpath','//*[@id="sex"]/label[2]/span[1]')

    def click_select_sex_girl(self):
        self.click(self.select_sex_girl_loc)

    select_sex_boy_loc = ('xpath', '//*[@id="sex"]/label[1]/span[1]')

    def click_select_sex_boy(self):
        self.click(self.select_sex_boy_loc)

    addtea_upload_photo_loc = ('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/span/div/span/button')

    def click_addtea_upload_photo(self):
        self.click(self.addtea_upload_photo_loc)

    addtea_cancel_btn_loc = ('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_addtea_cancel_btn(self):
        self.click(self.addtea_cancel_btn_loc)

    addtea_determine_btn_lco = ('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_addtea_determine_btn(self):
        self.click(self.addtea_determine_btn_lco)

    edittea_operating_btn_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[7]/td[7]/button')

    edittea_edit_teacher_loc = ('xpath','//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]')

    edittea_delete_teacher_loc = ('xpath','//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]')

    def move_edittea_operating_btn(self):
        self.move(self.edittea_operating_btn_loc,self.edittea_edit_teacher_loc)

    def move_deletetea_operating_btn(self):
        self.move(self.edittea_operating_btn_loc,self.edittea_delete_teacher_loc)

    edittea_upload_photo_loc = ('xpath','/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/span/div/span/button')

    def click_edittea_upload_photo(self):
        self.click(self.edittea_upload_photo_loc)

    edittea_cancel_btn_loc = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[1]')

    def click_edittea_cancel_btn(self):
        self.click(self.edittea_cancel_btn_loc)

    edittea_detemine_btn_lco = ('xpath','/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[2]')

    def click_edittea_detemine_btn(self):
        self.click(self.edittea_detemine_btn_lco)

    dialog_delete_teacher_cancel_loc = ('xpath','/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[1]')

    def click_dialog_delete_teacher_cancel(self):
        self.click(self.dialog_delete_teacher_cancel_loc)

    dialog_delete_teacher_determine_loc = ('xpath', '/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[2]')

    def click_dialog_delete_teacher_determine(self):
        self.click(self.dialog_delete_teacher_determine_loc)

    previous_page_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[2]/a')

    def click_previous_page(self):
        self.click(self.previous_page_loc)

    next_page_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[4]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    spinner_select_row_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[5]/div[1]/div/span')

    def click_spinner_select_row(self):
        self.click(self.spinner_select_row_loc)

    input_jumperpage_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[5]/div[2]/input')

    def input_jumper_page(self):
        self.send_keys(self.input_jumperpage_loc, '2')

