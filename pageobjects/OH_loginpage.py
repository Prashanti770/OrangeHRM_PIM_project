import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

class OH_Loginpage(BaseDriver):
    #login page locators
    username_tbx_id = "txtUsername"
    password_tbx_id = "txtPassword"
    login_btn_id = "btnLogin"
    welcome_text_xp = "//a[@id='welcome']"
    logout_btn_lt ="Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self,user):
        self.wait_until_element_is_clickable(By.ID,self.username_tbx_id).clear()
        self.wait_until_element_is_clickable(By.ID,self.username_tbx_id).send_keys(user)

    def set_password(self,pwd):
        self.driver.find_element(By.ID,self.password_tbx_id).clear()
        self.driver.find_element(By.ID, self.password_tbx_id).send_keys(pwd)

    def login_click(self):
        self.wait_until_element_is_clickable(By.ID,self.login_btn_id).click()

    def welcome_msg(self):
        welcome_link = self.wait_until_element_is_clickable(By.XPATH,self.welcome_text_xp).text
        return welcome_link

    def logout_click(self):
        self.wait_until_element_is_clickable(By.XPATH, self.welcome_text_xp).click()
        self.wait_until_element_is_clickable(By.LINK_TEXT,self.logout_btn_lt).click()



