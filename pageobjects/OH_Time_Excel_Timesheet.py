import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver
from utilities import XLutilities


class Excel_Time(BaseDriver):
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

    def timesheet(self):
        time = self.driver.find_element(By.ID, self.time_id)
        time_sheet = self.driver.find_element(By.ID, self.timesheets_id)
        mytime_sheet=self.driver.find_element(By.ID,self.mytimesheet_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(time).move_to_element(time_sheet).move_to_element(mytime_sheet).click().perform()
        self.driver.find_element(By.ID,self.edit_id).click()

    def excel_timedata(self):
        path = ".\\testdata\\Timesheet.xlsx"
        rows = XLutilities.getRowCount(path, 'timesheet')
        cols = XLutilities.getColumnCount(path, 'timesheet')
        # print("row count", rows)
        # print("cols count",cols)
        # for i in range (1, rows):
        #     for c in range(1, cols+1):
        #      val = XLutilities.readData(path, 'timesheet',i,c)
        #      print(val, end="   ")
        #     print()
        time_table = "//table[@class='table']/tbody"
        time_tbcols = "//table[@class='table']/tbody/tr/td"
        time_tbrows = "//table[@class='table']/tbody/tr"
        time_tb_br1 = "["
        time_tb_br2 = "]"
        time_tb_cols = "/td"
        time_tb_col_tag = "td"
        time_tb_row_tag = "tr"
        time_td_input = "/input[1]"
        time_td_select = "//select[@class='projectActivity']"
        wt_table = self.driver.find_element(By.XPATH, time_table)
        wt_rows = wt_table.find_elements(By.XPATH, time_tb_row_tag)
        wt_rowcount = len(wt_rows)

        for r in range(2, rows):

            projectname = XLutilities.readData(path,'timesheet',r,1)
            activityname = XLutilities.readData(path,'timesheet',r,2)
            mon = XLutilities.readData(path,'timesheet',r,3)
            tue = XLutilities.readData(path,'timesheet',r,4)
            wed = XLutilities.readData(path,'timesheet',r,5)
            thu = XLutilities.readData(path,'timesheet',r,6)
            fri = XLutilities.readData(path,'timesheet',r,7)
            # XLutilities.writeData(path, 'timesheet', r, 8, "row added successfully")
            # print("webtable row count",wt_rowcount)
            wt_r = 0
            for wt_r in range(0,wt_rowcount):
                print("initial count",wt_r)

                wti_r = wt_r+1
            # wti_r=1
                print("increement count",wti_r)
                col_value1 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(
                        2) + time_tb_br2 + time_td_input

                drp_down3 = self.driver.find_element(By.XPATH, col_value1)
                print("xpath",drp_down3.text)
                drp_down3.clear()
                # print(projectname)
                drp_down3.send_keys(projectname)
                drp_down3.send_keys(Keys.ARROW_DOWN)
                drp_down3.send_keys(Keys.ENTER)

                # activity value
                # print(activityname)
                col_value2 = time_tbrows + time_tb_br1+ str(wti_r)+time_tb_br2+time_tb_cols+time_tb_br1+ str(3)+time_tb_br2+time_td_select

                # print(col_value2)
                drp_down2 = self.driver.find_element(By.XPATH, col_value2)
                # drp_down2 = Select(self.driver.find_element(By.XPATH, col_value2))
                # drp_down2.select_by_visible_text(activityname)
                # # drp_down2.select_by_index(activityname)
                # # drp_down2.select_by_value(activityname)

                drp_down2.send_keys(activityname)
            # drp_down2.send_keys(Keys.ARROW_DOWN)
                time.sleep(3)
                drp_down2.send_keys(Keys.ENTER)

                # mon tue.....values
                col_value3 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(4) + time_tb_br2 + time_td_input
                self.driver.find_element(By.XPATH, col_value3).send_keys(mon)
                col_value4 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(5) + time_tb_br2 + time_td_input
                self.driver.find_element(By.XPATH, col_value4).send_keys(tue)
                # col_value5 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(6) + time_tb_br2 + time_td_input
                # self.driver.find_element(By.XPATH,col_value5).send_keys(wed)
                # col_value6 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(7) + time_tb_br2 + time_td_input
                # self.driver.find_element(By.XPATH, col_value6).send_keys(thu)
                # col_value7 = time_tbrows + time_tb_br1 + str(wti_r) + time_tb_br2 + time_tb_cols + time_tb_br1 + str(8) + time_tb_br2 + time_td_input
                # self.driver.find_element(By.XPATH, col_value7).send_keys(fri)
                # save_btn_xpath = "//input[@id='submitSave']"
                # self.driver.find_element(By.XPATH,save_btn_xpath).click()
                # break
                # self.driver.find_element(By.XPATH,"//input[@id='btnEdit']").click()
                self.driver.find_element(By.XPATH, self.addrow_xp).click()
                # if col_value1 == "":
                #     self.driver.find_element(By.XPATH, self.addrow_xp).click()
                # break
                print(wti_r, "row inserted successfully")
                wti_r+=1
                print("initial increement count", wti_r)

            # break
        # self.driver.find_element(By.XPATH, self.addrow_xp).click()
            # break







