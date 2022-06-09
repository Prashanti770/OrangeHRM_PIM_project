import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver

class OH_PIM_Emp_Perdetails(BaseDriver):
#Personal Details locators
    pd_edit_btn = "//input[@id='btnSave']"
    form_xp = "//form[@id='frmEmpPersonalDetails']"
    tag_input_xp = "input"
    Nationality_xp = "//select[@id='personal_cmbNation']"
    radio_m = "//input[@id='personal_optGender_1']"
    radio_f = "//input[@id='personal_optGender_2']"
    led_calendar_tb = "//input[@id='personal_txtLicExpDate']"
    pd_save = "//input[@id='btnSave']"
#custom fields locators
    cf_edit = "//input[@id='btnEditCustom']"
    cf_select = "//select[@name='custom1']"
    cf_save = "//input[@name='btnEditCustom']"
#Attachments locators
    att_add_btn = "//input[@id='btnAddAttachment']"
    att_choose = "//input[@id='ufile']"
    att_cmnt = "//textarea[@id='txtAttDesc']"
    att_upload = "//input[@id='btnSaveAttachment']"
    att_cancel = "//input[@id='cancelButton']"
#Edit Employee picture Locators
    pic_xp = "//img[@id='empPic']"
    pic_choose = "//input[@id='photofile']"
    pic_upload_btn = "//input[@id='btnSave']"
    pic_delete_btn = "//input[@id='btnDelete']"
    del_popup_ok = "//input[@id='btnYes']"
    del_popup_cancel = "//input[@id='btnNo']"
    # del_popup_close = "//div[@id='displayAbout']/div/a"
    del_popup_close = "×"
    del_success = ""


    def __init__(self,driver):
        self.driver = driver

    def personaldetails_verify(self):
        pd_form= self.driver.find_element(By.XPATH,self.form_xp)
        all_text= pd_form.find_elements(By.TAG_NAME,self.tag_input_xp)
        fsize = len(all_text)
        print(fsize)
        for i in all_text:
            verify = i.is_enabled()
            text = i.get_attribute("name")
            if verify == False:
                print(text,verify, "Element is Disabled")
            else:
                print(text,verify, "Element is enabled")

    def edit_pd(self):
        self.driver.find_element(By.XPATH,self.pd_edit_btn).click()

    def edit_pdetails(self,name,radio_value):
       nation_value = Select(self.driver.find_element(By.XPATH,self.Nationality_xp))
       nation_value.select_by_visible_text(name)

       if radio_value == "F":
           self.driver.find_element(By.XPATH,self.radio_f).click()
       elif radio_value == "M":
           self.driver.find_element(By.XPATH,self.radio_m).click()

    def edit_calendar(self,date):
        self.driver.find_element(By.XPATH, self.led_calendar_tb).clear()
        dtb = self.driver.find_element(By.XPATH,self.led_calendar_tb)
        dtb.send_keys(date)
        dtb.send_keys(Keys.ENTER)

    def save_pd(self):
        self.driver.find_element(By.XPATH, self.pd_save).click()

    def edit_cfields(self,cfvalue):
        self.driver.find_element(By.XPATH,self.cf_edit).click()
        cf_value = Select(self.driver.find_element(By.XPATH,self.cf_select))
        cf_value.select_by_value(cfvalue)
        self.driver.find_element(By.XPATH,self.cf_save).click()

    def upload_attach_add(self, file, cmt_txt):
        self.driver.find_element(By.XPATH, self.att_add_btn).click()
        self.driver.find_element(By.XPATH, self.att_choose).send_keys(file)
        self.driver.find_element(By.XPATH, self.att_cmnt).send_keys(cmt_txt)

    def upload_attach_upload(self):
        self.driver.find_element(By.XPATH, self.att_upload).click()

    def upload_attach_cancel(self):
        self.driver.find_element(By.XPATH, self.att_cancel).click()

    def edit_emp_pic(self):
        self.driver.find_element(By.XPATH, self.pic_xp).click()
    def edit_emppic_upload(self,emppic):
        self.driver.find_element(By.XPATH, self.pic_choose).send_keys(emppic)
        self.driver.find_element(By.XPATH, self.pic_upload_btn).click()
    def edit_emppic_delete(self):
        self.driver.find_element(By.XPATH, self.pic_delete_btn).click()

    def del_ok(self):
        self.driver.find_element(By.XPATH,self.del_popup_ok).click()
        time.sleep(3)

    def del_cancel(self):
        self.driver.find_element(By.XPATH,self.del_popup_cancel).click()

    def del_close(self):
        # time.sleep(5)
        self.wait_until_element_is_clickable(By.LINK_TEXT,self.del_popup_close).click()

    def cnf_del_success(self):
        self.data = self.driver.find_element(By.XPATH, self.del_success).text
        # print(self.data)
        if "Delete" in self.data:
            print("Deleted Successfully")
