from common.basics import Crazy

class UserManagementPage(Crazy):
    '''用户管理页面'''

    user_management_loc = ('xpath','//*[@id="root"]/div/div[2]/div[1]/div/div/ul/li[9]/a')

    def click_user_management(self):
        self.click(self.user_management_loc)

    start_end_date_loc = ('xpath', '//*[@id="start"]/span')

    def click_start_end_date(self):
        self.click(self.start_end_date_loc)

    select_year_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/span/a[1]')

    def click_select_year(self):
        self.click(self.select_year_loc)

    select_year_item_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/a')

    def click_select_year_item(self):
        self.click(self.select_year_item_loc)

    select_month_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/span/a[2]')

    def click_select_month(self):
        self.click(self.select_month_loc)

    select_month_item_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/a')

    def click_select_month_item(self):
        self.click(self.select_month_item_loc)

    start_date_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div')

    def click_start_data(self):
        self.click(self.start_date_loc)

    end_date_loc = ('xpath','//*[@id="createTimeRangePicker"]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[4]/div')

    def click_end_date(self):
        self.click(self.end_date_loc)

    user_name_loc = ('xpath','//*[@id="queryString"]')

    def input_user_name(self):
        self.send_keys(self.user_name_loc,'小')

    query_btn_loc = ('xpath','//*[@id="mainContainer"]/div[2]/div[2]/div[1]/div/div[3]/div/div/button')

    def click_query_btn(self):
        self.click(self.query_btn_loc)

    previous_page_loc = ('xpath', '//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[2]/a')

    def click_previous_page(self):
        self.click(self.previous_page_loc)

    next_page_loc = ('xpath', '//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[7]/a')

    def click_next_page(self):
        self.click(self.next_page_loc)

    spinner_select_row_loc = ('xpath', '//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[8]/div[1]/div/span')

    def click_spinner_select_row(self):
        self.click(self.spinner_select_row_loc)

    input_jumperpage_loc = ('xpath', '//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[8]/div[2]/input')

    def input_jumper_page(self):
        self.send_keys(self.input_jumperpage_loc, '2')

    input_jumper_page02_loc = ('xpath', '//*[@id="mainContainer"]/div[2]/div[2]/div[2]/div/div/ul/li[8]/div[2]/input')

    def input_jumper_page02(self):
        self.send_keys(self.input_jumper_page02_loc, '2')

    page_number_loc = ('xpath','//*[@id="mainContainer"]/div[3]/div[2]/div[2]/div/div/ul/li[6]/a')

    def select_page_number(self):
        self.click(self.page_number_loc)

