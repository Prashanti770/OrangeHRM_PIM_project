import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver

class OH_PIM_EmpList_Add(BaseDriver):
#Add Employee locators
    add_emp_fname_fn = "//input[@id='firstName']"
    add_emp_fname_mn = "//input[@id='middleName']"
    add_emp_fname_ln = "//input[@id='lastName']"
    add_emp_photo = "//input[@id='photofile']"
#Create login locators
    add_emp_createlogin = "//input[@id='chkLogin']"
    addemp_username = "//input[@id='user_name']"
    addemp_password = "//input[@id='user_password']"
    addemp_cnfrm_pwd = "//input[@id='re_password']"
    addemp_status = "//select[@id='status']"

#Save button locators
    add_emp_savebtn = "//input[@id='btnSave']"

    def __init__(self, driver):
        self.driver = driver

    def emplist_addemp(self,fn,mn,ln,photo_path):
        # print("Add employee")

        # self.wait_until_element_is_clickable(By.XPATH,self.add_emp_fname_fn).send_keys(fn)
        self.driver.find_element(By.XPATH,self.add_emp_fname_fn).send_keys(fn)
        self.wait_until_element_is_clickable(By.XPATH, self.add_emp_fname_mn).send_keys(mn)
        self.wait_until_element_is_clickable(By.XPATH, self.add_emp_fname_ln).send_keys(ln)
        self.wait_until_element_is_clickable(By.XPATH, self.add_emp_photo).send_keys(photo_path)

    def addemp_createlogin_btn(self,un,pwd,cpwd,status):

        self.wait_until_element_is_clickable(By.XPATH, self.add_emp_createlogin).click()
        self.wait_until_element_is_clickable(By.XPATH, self.addemp_username).send_keys(un)
        self.wait_until_element_is_clickable(By.XPATH, self.addemp_password).send_keys(pwd)
        self.wait_until_element_is_clickable(By.XPATH, self.addemp_cnfrm_pwd).send_keys(cpwd)
        sel_status=Select(self.wait_until_element_is_clickable(By.XPATH, self.addemp_status))
        sel_status.select_by_visible_text(status)

    def addemp_savebtn(self):
        self.wait_until_element_is_clickable(By.XPATH, self.add_emp_savebtn).click()





