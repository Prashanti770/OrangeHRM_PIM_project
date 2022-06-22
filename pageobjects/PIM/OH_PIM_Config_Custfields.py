import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver

class OH_PIM_Configuration_CF(BaseDriver):

    #Configurations Custom Fields Locators
    confg_cus_fields = "//a[@id='menu_pim_listCustomFields']"
    confg_dcf_add = "//input[@id='buttonAdd']"
    confg_dcf_delete = "//input[@id='buttonRemove']"
    confg_dcf_text ="//span[@id='fieldsleft']"
    confg_dcf_table ="//table[@id='customFieldList']"
    confg_dcf_rows = "//table[@id='customFieldList']/tbody/tr"
    dcf_row = "/tbody/tr"
    confg_dcf_row_tag ="tr"
    confg_dcf_cols_tag = "td"
    confg_dcf_cols ="/td"
    br1 = "["
    br2 = "]"
    chckbx_xpath ="//preceding-sibling::td//input[@type='checkbox']"
    add_cf_name ="//input[@id='customField_name']"
    add_cf_screen ="//select[@id='customField_screen']"
    add_cf_type ="//select[@id='customField_type']"
    add_cf_save ="//input[@id='btnSave']"
    add_cf_cancel ="//input[@id='btnCancel']"
    del_cf_ok ="//input[@id='dialogDeleteBtn']"
    del_cf_cancel ="//input[@class='btn reset']"
    del_cf_close ="//div[@id='deleteConfModal']/div[1]/a"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def confg_customfields(self):
        self.wait_until_element_is_clickable(By.XPATH, self.confg_cus_fields).click()

    def dcf_add(self):
        self.wait_until_element_is_clickable(By.XPATH, self.confg_dcf_add).click()

    def dcf_addvalues(self,name,scrn,type):
        self.wait_until_element_is_clickable(By.XPATH, self.add_cf_name).send_keys(name)
        sel_screen=Select(self.wait_until_element_is_clickable(By.XPATH, self.add_cf_screen))
        sel_screen.select_by_visible_text(scrn)
        sel_type = Select(self.wait_until_element_is_clickable(By.XPATH, self.add_cf_screen))
        sel_type.select_by_visible_text(type)

    def acf_save(self):
        self.wait_until_element_is_clickable(By.XPATH, self.add_cf_save).click()

    def acf_cancel(self):
        self.wait_until_element_is_clickable(By.XPATH, self.add_cf_cancel).click()

    def dcf_table_search_del(self,name):
        #//table[@id='customFieldList']/tbody/tr[1]/td[2]
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.confg_dcf_table)
        rows = result_table.find_elements(By.TAG_NAME, self.confg_dcf_row_tag)
        rows_count = len(rows)
        print(rows_count)
        print(
            "Custom Field Name" + "      " + "Screen" + "       " + "Field Type")
        for r in range(1, rows_count):
            # cols = rows[r].find_elements(By.TAG_NAME, self.confg_dcf_cols)
            # cols_count = len(cols)
            # print(cols_count)
            col_value = self.driver.find_element(By.XPATH, self.confg_dcf_rows + self.br1 + str(r)
                                                     + self.br2 + self.confg_dcf_cols + self.br1
                                                     + str(2) + self.br2)
            chkvalue_xpath = self.confg_dcf_rows + self.br1 + str(r) + self.br2 + self.confg_dcf_cols + self.chckbx_xpath
            value = col_value.text
            if value == name:
                print(name)
                self.driver.find_element(By.XPATH, chkvalue_xpath).click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.confg_dcf_delete).click()

            else:
                print("No Records Found")

        print()


    def del_ok(self):
        self.driver.find_element(By.XPATH,self.del_cf_ok).click()
        time.sleep(3)

    def del_cancel(self):
        self.driver.find_element(By.XPATH,self.del_cf_cancel).click()

    def del_close(self):
        self.driver.find_element(By.XPATH,self.del_cf_close).click()

    def dcf_verify_count(self):
        text = self.wait_until_element_is_clickable(By.XPATH, self.confg_dcf_text).text
        print(text)
        # table = self.wait_until_element_is_clickable(By.XPATH, self.confg_dcf_table)
        # row = table.find_elements(By.XPATH, self.dcf_row)
        row = self.driver.find_elements(By.XPATH,self.confg_dcf_rows)
        row_count = len(row)
        print(row_count)
        a =10
        final_count = a - row_count
        print(final_count)
        fc =str(final_count)
        if fc in text:
            print("count matches")
        else:
            print("count doesnt match")

    def table_print(self):
        # table = self.wait_until_element_is_clickable(By.XPATH, self.confg_dcf_table)
        # row = table.find_elements(By.XPATH, self.dcf_row)
        row = self.driver.find_elements(By.XPATH, self.confg_dcf_rows)
        row_count1 = len(row)
        print("rows count",row_count1)
        for r in range(1, row_count1):
            cols = row[r].find_elements(By.TAG_NAME, self.confg_dcf_cols_tag)
            cols_count1 = len(cols)
            print("columns count",cols_count1)
            for c in range(2, cols_count1):
                col_value = self.driver.find_element(By.XPATH, self.confg_dcf_rows + self.br1 + str(r)
                                                     + self.br2 + self.confg_dcf_cols + self.br1
                                                     + str(c) + self.br2)
                value = col_value.text
                print(value,end="      ")
