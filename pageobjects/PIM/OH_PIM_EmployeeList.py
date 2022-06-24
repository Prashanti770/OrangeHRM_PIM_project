import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver

class OH_PIM_EmpList(BaseDriver):

# PIM Module and Employee List locators
    pim_btn_id = "menu_pim_viewPimModule"
    pim_emplist_id ="menu_pim_viewEmployeeList"
    pim_addemp_xp = "//a[@id='menu_pim_addEmployee']"

#Employee info for Search Locators
    empinfo_empname_xp="//input[@id='empsearch_employee_name_empName']"
    empinfo_id_id ="empsearch_id"
    empinfo_employement_status_id = "empsearch_employee_status"
    empinfo_include_id = "empsearch_termination"
    empinfo_supervisorlist_id ="empsearch_supervisor_name"
    empinfo_jobtitle_xp ="//select[@id='empsearch_job_title']"
    empinfo_subunit_id ="empsearch_sub_unit"
    empinfo_search_btnxp ="//input[@id='searchBtn']"
    empinfo_reset_btnxp ="//input[@id='resetBtn']"

#Employee List ADD button locator
    elist_addbtn = "//input[@id='btnAdd']"

#Table data search results locators
    empinfo_table ="//table[@id='resultTable']"
    empinfo_tbcols ="//table[@id='resultTable']//tbody/tr/td"
    empinfo_tbrows = "//table[@id='resultTable']//tbody/tr"
    empinfo_tb_br1 = "["
    empinfo_tb_br2 = "]"
    empinfo_tb_cols ="/td"
    tb_col_tag = "td"
    tb_row_tag = "tr"
    col_click_xp = "/a"
    # tb_xp = "//table[@id='customers']//tbody/tr[" + str(r) + "]/td[1]"

#Delete Employee locators
    elist_delete = "//input[@id='btnDelete']"
    loc_chkbox_xp = "//preceding-sibling::td//input"
    del_popup_ok = "//input[@id='dialogDeleteBtn']"
    del_popup_cancel = "//input[@class='btn cancel']"
    del_popup_close = "//div[@id='deleteConfModal']/div[1]/a"
    del_conf_text = "//div[@id='deleteConfModal']/div[2]/p"

# Successfully messages locators
    del_success = "//form[@id='frmList_ohrmListComponent']"

#Edit Personal info locators


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def oh_pim(self): #PIM module Click
        self.wait_until_element_is_clickable(By.ID,self.pim_btn_id).click()

    def oh_pim_emplist(self): #Click on Employee list
        self.wait_until_element_is_clickable(By.ID,self.pim_emplist_id).click()

    def oh_pim_addemp_mod(self): #Add Employee module
        self.wait_until_element_is_clickable(By.XPATH,self.pim_addemp_xp).click()

    #Employee Search Info methods
    def empinfo_empname(self,empname):

        ele=self.wait_until_element_is_clickable(By.XPATH,self.empinfo_empname_xp)
        ele.clear()
        ele.send_keys(empname)
        ele.send_keys(Keys.ARROW_DOWN)
        ele.send_keys(Keys.ENTER)

    def empinfo_empid(self,emp_id):
        self.wait_until_element_is_clickable(By.ID, self.empinfo_id_id).clear()
        self.wait_until_element_is_clickable(By.ID, self.empinfo_id_id).send_keys(emp_id)

    def empinfo_empstatus(self):
        select_emp_status=Select(self.wait_until_element_is_clickable(By.ID,self.empinfo_employement_status_id))
        select_emp_status.select_by_index(3)

    def empinfo_include(self):
        select_include=Select(self.wait_until_element_is_clickable(By.ID,self.empinfo_include_id))
        select_include.select_by_visible_text('Past Employees Only')

    def empinfo_supervisorname(self, supname):
        ele_suprv = self.driver.find_element(By.ID, self.empinfo_supervisorlist_id)
        ele_suprv.send_keys(supname)
        ele_suprv.send_keys(Keys.ARROW_DOWN)
        ele_suprv.send_keys(Keys.ENTER)

    def empinfo_jobtitle(self,jobtitle_value):
        jobtitle = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_jobtitle_xp)
        select_jobtitle = Select(jobtitle)
        jobtitle_options = select_jobtitle.options
        # print(len(jobtitle_options))
        for option in jobtitle_options:
            opt_value = option.text
            # print(opt_value)
            if opt_value == jobtitle_value:
                select_jobtitle.select_by_visible_text(jobtitle_value)
            # else:
            #     print("error")

    def empifno_subunit(self):
        select_subunit = Select(self.wait_until_element_is_clickable(By.ID, self.empinfo_subunit_id))
        select_subunit.select_by_value('5')

    def empinfo_search(self):
        self.driver.find_element(By.XPATH,self.empinfo_search_btnxp).click()

    def empinfo_reset(self):
        self.driver.find_element(By.XPATH,self.empinfo_reset_btnxp).click()

    def empinfo_add(self): #Employee List ADD button
        self.wait_until_element_is_clickable(By.XPATH, self.elist_addbtn).click()


    def getrow_count(self):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        return len(rows)
        # rows_count = len(rows)
        # print(rows_count)

    def getcol_count(self):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        cols1 = result_table.find_elements(By.TAG_NAME, self.empinfo_tb_cols)
        cols_count1 = len(cols1)
        print(cols_count1)


    def table_searchempbyId(self, id):
        # flag = False
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        # rows_count = len(rows)
        # print(rows_count)
        print("Id" + "      " + "Firstname" + "       " + "Lastname" + "       " + "Jobtitle" + "       " + "Employement status"
            + "       " + "Sub unit" + "       " + "Supervisor")
        for r in range(1, self.getrow_count()):
            cols = rows[r].find_elements(By.TAG_NAME, self.tb_col_tag)
            cols_count = len(cols)
            # print(cols_count)
            for c in range(1, cols_count):
                col_value = self.driver.find_element(By.XPATH, self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)
                                                     + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1
                                                     + str(2) + self.empinfo_tb_br2)
                value = col_value.text
                if value == id:
                    print(cols[c].text, end="         ")
                    # flag = True
                    # break
                else:
                    print("No Records Found")

            print()
        # return flag


    def table_link_click(self, id):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)

        for r in range(1, self.getrow_count()):
            col_value = self.driver.find_element(By.XPATH, self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)
                                                     + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1
                                                     + str(2) + self.empinfo_tb_br2)
            value = col_value.text
            if value == id:
                self.driver.find_element(By.XPATH,self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)
                                             + self.empinfo_tb_br2 + self.empinfo_tb_cols
                                             +self.col_click_xp).click()
                break

    def empinfo_emp_delete(self, del_value):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)
        for r in range(1, rows_count):

            chkvalue_xpath = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1 + str(2) + self.empinfo_tb_br2
            chkvalue_xpath2 = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.loc_chkbox_xp
            # "//table[@id='resultTable']//tbody/tr["+str(r)+"]/td//preceding-sibling::td//input"
            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            # print(checkbox_value)
            if checkbox_value == del_value:
                print(del_value)
                self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.elist_delete).click()


    def del_conf_msg(self):
        conf_text = self.driver.find_element(By.XPATH, self.del_conf_text).text
        if "Delete" in conf_text:
            print(conf_text)

    def del_ok(self):
        self.driver.find_element(By.XPATH,self.del_popup_ok).click()
        time.sleep(3)

    def del_cancel(self):
        self.driver.find_element(By.XPATH,self.del_popup_cancel).click()

    def del_close(self):
        self.driver.find_element(By.XPATH,self.del_popup_close).click()


    def cnf_del_success(self):
        self.data = self.driver.find_element(By.XPATH, self.del_success).text
        # print(self.data)
        if "Delete" in self.data:
            print("Deleted Successfully")





