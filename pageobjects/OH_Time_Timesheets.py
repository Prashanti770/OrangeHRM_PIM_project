import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
class Time(BaseDriver):
    admin_btn_id = "menu_admin_viewAdminModule"
    time_id="menu_time_viewTimeModule"
    timesheets_id="menu_time_Timesheets"
    mytimesheet_id="menu_time_viewMyTimesheet"
    edit_id="btnEdit"
    empinfo_table = "//table[@class='table']"

    empinfo_tbcols = "//table[@class='table']//tbody/tr/td"
    empinfo_tbrows = "//table[@class='table']//tbody/tr"
    empinfo_tb_br1 = "["
    empinfo_tb_br2 = "]"
    empinfo_tb_cols = "/td"
    tb_col_tag = "td"
    tb_row_tag = "tr"
    project_id="initialRows_0_projectName"
    activity_id="initialRows_0_projectActivityName"
    mon6_xp = "//input[@id='initialRows_0_0']"
    tues_id="initialRows_0_1"
    wed_xp = "//input[@id='initialRows_0_2']"
    thu_xp = "//input[@id='initialRows_0_3']"
    fri_xp = "//input[@id='initialRows_0_4']"
    save_btn = "//input[@id='submitSave']"
    addrow_xp = "//input[@id='btnAddRow']"
    employeetimesheet_id="menu_time_viewEmployeeTimesheet"
    employeename_id="employee"
    viewbtn_id="btnView"
    addtimesheet_id="btnAddTimesheet"
    calender_id="time_date"
    title_xp="//*[@id='ui-datepicker-div']/div/div"
    calenbox_xp="//*[@id='ui-datepicker-div']/table"
    ok_id="addTimesheetBtn"

    def __init__(self, driver):
        self.driver = driver

    def time_login(self):
        admin= self.driver.find_element(By.ID,self.admin_btn_id)
        time=self.driver.find_element(By.ID,self.time_id)
        time_sheet=self.driver.find_element(By.ID,self.timesheets_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(time).move_to_element(time_sheet).click().perform()
    def timesheet(self):
        time = self.driver.find_element(By.ID, self.time_id)
        time_sheet = self.driver.find_element(By.ID, self.timesheets_id)
        mytime_sheet=self.driver.find_element(By.ID,self.mytimesheet_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(time).move_to_element(time_sheet).move_to_element(mytime_sheet).click().perform()
        self.driver.find_element(By.ID,self.edit_id).click()


    sheet = ["prjname",'activity','mon','tues']
    def table_data(self,prjname,activity,mon,tues):

                # self.driver.find_element(By.XPATH, self.addrow_xp).click()
                drp_down1 = self.driver.find_element(By.ID, self.project_id)
                drp_down1.clear()
                drp_down1.send_keys(prjname)
                drp_down1.send_keys(Keys.ARROW_DOWN)
                drp_down1.send_keys(Keys.ENTER)
                drp_down = self.driver.find_element(By.ID, self.activity_id)
                drp_down.click()
                time.sleep(3)
                drp_down.send_keys(activity)
                drp_down.send_keys(Keys.ENTER)

                self.driver.find_element(By.XPATH,self.mon6_xp).send_keys(mon)
                self.driver.find_element(By.ID,self.tues_id).send_keys(tues)

                # break

    def excel_table_data(self,prjname): #,mon,tue,wed,thu,fri
        #//table[@class='table']/tbody/tr[1]/td[8]
        time_table = "//table[@class='table']/tbody"
        time_tbcols = "//table[@class='table']/tbody/tr/td"
        time_tbrows = "//table[@class='table']/tbody/tr"
        time_tb_br1 = "["
        time_tb_br2 = "]"
        time_tb_cols = "/td"
        time_tb_col_tag = "td"
        time_tb_row_tag = "tr"
        time_td_input = "/input[1]"
        table = self.driver.find_element(By.XPATH,time_table)
        rows= table.find_elements(By.XPATH,time_tb_row_tag)
        rowcount = len(rows)
        for r in range(1,rowcount):
            col_value1 = time_tbrows + time_tb_br1+ str(r)+time_tb_br2+time_tb_cols+time_tb_br1+ str(2)+time_tb_br2+time_td_input
            drp_down3 = self.driver.find_element(By.XPATH, col_value1)
            drp_down3.clear()
            # print(prjname)
            drp_down3.send_keys(prjname)
            drp_down3.send_keys(Keys.ARROW_DOWN)
            drp_down3.send_keys(Keys.ENTER)
            self.driver.find_element(By.XPATH, self.addrow_xp).click()

            # # activity value
            # col_value2 = time_tbrows + time_tb_br1+ str(r)+time_tb_br2+time_tb_cols+time_tb_br1+ str(3)+time_tb_br2+time_td_input
            # drp_down2 = self.driver.find_element(By.XPATH, col_value2)
            # drp_down2.send_keys("actname")
            # drp_down2.send_keys(Keys.ENTER)

            # mon tue.....values
            # col_value3 = time_tbrows + time_tb_br1 + str(r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(4) + time_tb_br2 + time_td_input
            # self.driver.find_element(By.XPATH, col_value3).send_keys(mon)
            # col_value4 = time_tbrows + time_tb_br1 + str(r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(5) + time_tb_br2 + time_td_input
            # self.driver.find_element(By.XPATH, col_value4).send_keys(tue)
            # col_value5 = time_tbrows + time_tb_br1 + str(r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(6) + time_tb_br2 + time_td_input
            # self.driver.find_element(By.XPATH,col_value5).send_keys(wed)
            # col_value6 = time_tbrows + time_tb_br1 + str(r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(7) + time_tb_br2 + time_td_input
            # self.driver.find_element(By.XPATH, col_value6).send_keys(thu)
            # col_value7 = time_tbrows + time_tb_br1 + str(r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(8) + time_tb_br2 + time_td_input
            # self.driver.find_element(By.XPATH, col_value7).send_keys(fri)
            # time.sleep(2)
            # self.driver.find_element(By.XPATH,self.addrow_xp).click()
            # if col_value1 is None:
            #     print(col_value1)
            # break

    def employeetimesheet(self,name):
        time= self.driver.find_element(By.ID, self.time_id)
        time_sheet = self.driver.find_element(By.ID, self.timesheets_id)
        employeetime_sheet = self.driver.find_element(By.ID, self.employeetimesheet_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(time).move_to_element(time_sheet).move_to_element(employeetime_sheet).click().perform()
        self.driver.find_element(By.ID,self.employeename_id).clear()
        self.driver.find_element(By.ID,self.employeename_id).send_keys(name)
        self.driver.find_element(By.ID,self.employeename_id).send_keys(Keys.ENTER)
       #time.sleep(3)
        self.driver.find_element(By.ID, self.viewbtn_id).click()
        self.driver.find_element(By.ID,self.addtimesheet_id).click()
        self.driver.find_element(By.ID,self.calender_id).click()
        self.driver.find_element(By.XPATH,self.title_xp).click()
        self.driver.find_element(By.XPATH,self.calenbox_xp).click()
        self.driver.find_element(By.ID,self.ok_id).click()
