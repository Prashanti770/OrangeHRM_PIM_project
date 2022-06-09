from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

class OH_PIM_Contactdetails(BaseDriver):

    #Contact Details Form
    form_xp = "//form[@id='frmEmpContactDetails']"
    tag_input_xp = "input"

    #Contact Details Locators
    contactdet_btn_lt = "Contact Details"
    condet_edit_btn = "//input[@id='btnSave']"
    condet_addstrt1 = "//input[@id='contact_street1']"
    condet_city = "//input[@id='contact_city']"
    condet_state = "//input[@id='contact_province']"
    condet_mobileno = "//input[@id='contact_emp_mobile']"
    condet_save_btn ="//input[@id='btnSave']"

    #contact details Attachements
    condet_attach = "//input[@id='btnAddAttachment']"
    condet_att_choose ="//input[@id='ufile']"
    condet_att_comment = "//textarea[@id='txtAttDesc']"
    condet_att_upload_btn ="//input[@id='btnSaveAttachment']"
    condet_att_cancel_btn ="//input[@id='cancelButton']"

    def __init__(self, driver):
        self.driver = driver

    def click_contdetails(self):
        self.driver.find_element(By.LINK_TEXT,self.contactdet_btn_lt).click()

    def contactdetails_verify(self):
        pd_form = self.driver.find_element(By.XPATH, self.form_xp)
        all_text = pd_form.find_elements(By.TAG_NAME, self.tag_input_xp)
        fsize = len(all_text)
        print(fsize)
        for i in all_text:
            verify = i.is_enabled()
            text = i.get_attribute("name")
            if verify == False:
                print(text, verify, "Element is Disabled")
            else:
                print(text, verify, "Element is enabled")

    def edit_contdetails(self):
        self.driver.find_element(By.XPATH,self.condet_edit_btn).click()

    def contdetails_fill(self,addr1,city,state,mobile):
        self.driver.find_element(By.XPATH, self.condet_addstrt1).send_keys(addr1)
        self.driver.find_element(By.XPATH, self.condet_city).send_keys(city)
        self.driver.find_element(By.XPATH, self.condet_state).send_keys(state)
        self.driver.find_element(By.XPATH, self.condet_mobileno).send_keys(mobile)
        self.driver.find_element(By.XPATH, self.condet_save_btn).click()

    def contdetails_attach_add(self,file,cmmnt):
        self.driver.find_element(By.XPATH, self.condet_attach).click()
        self.driver.find_element(By.XPATH, self.condet_att_choose).send_keys(file)
        self.driver.find_element(By.XPATH, self.condet_att_comment).send_keys(cmmnt)

    def contdetails_attach_upload(self):
        self.driver.find_element(By.XPATH, self.condet_att_upload_btn).click()

    def contdetails_attach_cancel(self):
        self.driver.find_element(By.XPATH, self.condet_att_cancel_btn).click()

