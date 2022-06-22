from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class OH_PIM_Configuration(BaseDriver):
    #Configurations Operational Fields Locators
    config_btn = "//a[@id='menu_pim_Configuration']"
    conf_optnl_fields ="//a[@id='menu_pim_configurePim']"
    conf_opf_form ="//form[@id='frmConfigPim']"
    conf_opf_checkbox = "//input[@type='checkbox']"
    conf_opf_edit = "//input[@id='btnSave']"
    conf_opf_chck1 = "//input[@id='configPim_chkShowSSN']"

    #Configurations Custom Fields Locators
    confg_cus_fields = "//a[@id='menu_pim_listCustomFields']"
    confg_dcf_add = "//input[@id='buttonAdd']"
    confg_dcf_delete = "//input[@id='buttonRemove']"
    confg_dcf_text ="//span[@id='fieldsleft']"
    confg_dcf_table ="//table[@id='customFieldList']"
    confg_dcf_rows ="/tbody/tr"
    add_cf_name ="//input[@id='customField_name']"
    add_cf_screen ="//select[@id='customField_screen']"
    add_cf_type ="//select[@id='customField_type']"
    add_cf_save ="//input[@id='btnSave']"
    add_cf_cancel ="//input[@id='btnCancel']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def configuration(self):
        self.wait_until_element_is_clickable(By.XPATH,self.config_btn).click()

    def optional_fields(self):
        self.wait_until_element_is_clickable(By.XPATH, self.conf_optnl_fields).click()

    def configure_PIM_verify(self):
        co_pim = self.wait_until_element_is_clickable(By.XPATH, self.conf_opf_form)
        co_pim_cb = co_pim.find_elements(By.XPATH,self.conf_opf_checkbox)

        for c in co_pim_cb:
            # print(c)
            verify = c.is_selected()
            # value = c.text
            value = c.get_attribute("name")
            # c1 = c.find_element(By.XPATH,"//li[@class='checkbox']")
            # c1 = c.find_element(By.XPATH,"//label")
            # value = c1.text
            if verify == True:
                print(value,verify, "Checkbox is Selected")
            else:
                print(value,verify, "Checkbox is not selected")

    def config_opf_edit(self):
        self.wait_until_element_is_clickable(By.XPATH,self.conf_opf_edit).click()
    def config_opf_check(self):
        self.wait_until_element_is_clickable(By.XPATH, self.conf_opf_chck1).click()


