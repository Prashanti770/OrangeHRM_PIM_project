import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

class OH_PIM_Configuration_TR(BaseDriver):
    config_termrsns_btn = "//a[@id='menu_pim_viewTerminationReasons']"
    tr_add_btn = "//input[@id='btnAdd']"
    tr_add_name ="//input[@id='terminationReason_name']"
    tr_add_save ="//input[@id='btnSave']"
    tr_add_cancel ="//input[@id='btnCancel']"
    tr_add_tr_table_rows="//table[@id='recordsListTable']//tbody//tr"
    tr_delete ="//input[@id='btnDel']"
    term_rsns_table = "//table[@id='recordsListTable']//tbody"
    term_rsns_row = "//tr"
    term_rsns_col ="//td"
    term_rsns_chckbox ="//input[@type='checkbox']"
    br1 ="["
    br2 ="]"
    tr_table_chckbox ="//preceding-sibling::td//input"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def termination_rsns(self):
        self.wait_until_element_is_clickable(By.XPATH, self.config_termrsns_btn).click()

    def ter_rsns_add(self):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_btn).click()

    def add_name(self,name):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_name).send_keys(name)

    def add_save(self):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_save).click()

    def add_cancel(self):
        self.wait_until_element_is_clickable(By.XPATH, self.tr_add_cancel).click()

    def add_tr_table_print(self):
        # text = self.driver.find_element(By.XPATH, "//h1[@id='saveFormHeading']").text
        # print(text)
        add_trtable_rows = self.driver.find_elements(By.XPATH,self.tr_add_tr_table_rows)
        add_rows_count = len(add_trtable_rows)
        print("Row count of Termination Reasons in Add are : ",add_rows_count)
        print("Name of Rows :")
        add_tr_table = []
        for ar in add_trtable_rows:
            row_value = ar.text
            add_tr_table.append(ar)
            print(row_value)
        return add_tr_table

    def tr_table(self):
        tr_table_rows = self.driver.find_elements(By.XPATH, self.tr_add_tr_table_rows)
        # tr_table = self.driver.find_element(By.XPATH, self.term_rsns_table)
        # tr_table_rows = tr_table.find_elements(By.XPATH, self.term_rsns_row)
        tr_rows_count = len(tr_table_rows)
        print("Row count of Termination Reasons are : ", tr_rows_count)
        print("Name of Rows :")
        tr_table =[]
        for r in tr_table_rows:
            cvalue =r.text
            tr_table.append(r)
            print(cvalue)
        # for r in range(1, tr_rows_count):
        #     col_value_xp = self.term_rsns_table+self.term_rsns_row + self.br1 + str(r) + self.br2 + self.term_rsns_col + self.br1 + str(2) + self.br2
        #     col_value = self.driver.find_element(By.XPATH,col_value_xp)
        #     cvalue = col_value.text
        #     tr_table.append(cvalue)
        #     print(cvalue)

        return tr_table

    def tr_table_delete(self,del_value):
        tr_table = self.driver.find_element(By.XPATH,self.term_rsns_table)
        tr_table_rows = tr_table.find_elements(By.XPATH,self.term_rsns_row)
        tr_rows_count = len(tr_table_rows)
        print("Row count of Termination Reasons are : ",tr_rows_count)
        # tr_table_cols = tr_table_rows.find_elements(By.XPATH,self.term_rsns_col)
        for r in range(1, tr_rows_count):
            chkvalue_xpath = self.term_rsns_table+self.term_rsns_row + self.br1 + str(r) + self.br2 + self.term_rsns_col + self.br1 + str(2) + self.br2
            chkvalue_xpath2 = self.term_rsns_table+self.term_rsns_row  + self.br1 + str(r) + self.br2 + self.term_rsns_col + self.tr_table_chckbox
          #"//table[@id='recordsListTable']//tbody//tr//td//preceding-sibling::td//input"
            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            # print(checkbox_value)
            if checkbox_value == del_value:
                print(del_value)
                self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.tr_delete).click()




