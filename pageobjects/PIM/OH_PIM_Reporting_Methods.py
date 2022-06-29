import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class OH_PIM_Configuration_RM(BaseDriver):
    rep_methods_btn ="//a[@id='menu_pim_viewReportingMethods']"
    rm_add_btn ="//input[@id='btnAdd']"
    rm_delete_btn ="//input[@id='btnDel']"
    rm_table_row="//table[@id='recordsListTable']/tbody/tr"
    rm_table_col ="/td"
    tr_add_name = "//input[@id='reportingMethod_name']"
    tr_add_save = "//input[@id='btnSave']"
    tr_add_cancel = "//input[@id='btnCancel']"
    table_chckbox = "//preceding-sibling::td//input"
    reprt_methods_chckbox = "//input[@type='checkbox']"
    br1 = "["
    br2 = "]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def reporting_methods(self):
        self.wait_until_element_is_clickable(By.XPATH, self.rep_methods_btn).click()

    def rm_add(self):
        self.wait_until_element_is_clickable(By.XPATH, self.rm_add_btn).click()

    def add_name(self, name):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_name).send_keys(name)

    def add_save(self):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_save).click()

    def add_cancel(self):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_cancel).click()

    def add_rm_table_print(self):
        # text = self.driver.find_element(By.XPATH,"//h1[@id='saveFormHeading']").text
        # print(text)
        add_trtable_rows = self.driver.find_elements(By.XPATH, self.rm_table_row)
        add_rows_count = len(add_trtable_rows)
        print("Row count of Termination Reasons in Add are : ", add_rows_count)
        print("Name of Rows :")
        add_tr_table = []
        for ar in add_trtable_rows:
            row_value = ar.text
            add_tr_table.append(ar)
            print(row_value)
        return add_tr_table

    def rm_table(self):
        table_rows = self.driver.find_elements(By.XPATH, self.rm_table_row)
        tr_rows_count = len(table_rows)
        print("Row count of Termination Reasons are : ", tr_rows_count)
        print("Name of Rows :")
        tr_table = []
        for r in table_rows:
            cvalue = r.text
            tr_table.append(r)
            print(cvalue)
        return tr_table

    def rm_table_delete(self, del_value):
        tr_table_rows = self.driver.find_elements(By.XPATH, self.rm_table_row)
        tr_rows_count = len(tr_table_rows)
        print("Row count of Termination Reasons are : ", tr_rows_count)
        # tr_table_cols = tr_table_rows.find_elements(By.XPATH,self.term_rsns_col)
        for r in range(1, tr_rows_count):
            chkvalue_xpath = self.rm_table_row + self.br1 + str(
                r) + self.br2 + self.rm_table_col + self.br1 + str(2) + self.br2
            chkvalue_xpath2 = self.rm_table_row + self.br1 + str(
                r) + self.br2 + self.rm_table_col + self.table_chckbox
            # "//table[@id='recordsListTable']//tbody//tr//td//preceding-sibling::td//input"
            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            # print(checkbox_value)
            if checkbox_value == del_value:
                print(del_value)
                self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                time.sleep(3)
                # self.driver.find_element(By.XPATH, self.rm_delete_btn).click()







