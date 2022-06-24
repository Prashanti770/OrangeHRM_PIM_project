from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

class OH_PIM_Configuration_DI(BaseDriver):
    confg_di_btn = "//a[@id='menu_admin_pimCsvImport']"
    csv_filedwnld = "//a[@class='download']"
    csv_di_text ="//ul[@class='disc']//li"
    csv_di_choose ="//input[@id='pimCsvImport_csvFile']"
    csv_di_upload ="//input[@id='btnSave']"
    csv_di_up_success ="//div[@class='inner']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def dataimport(self):
        self.wait_until_element_is_clickable(By.XPATH, self.confg_di_btn).click()

    def csvfile_dwnld(self):
        self.wait_until_element_is_clickable(By.XPATH, self.csv_filedwnld).click()

    def file_choose(self,fpath):
        file =self.wait_until_element_is_clickable(By.XPATH, self.csv_di_choose)
        file.send_keys(fpath)

    def csvdi_text(self):
        l = self.driver.find_element(By.XPATH,"//ul[@class='disc']").text
        print("Instructions list",l)
        # di_list = self.driver.find_elements(By.XPATH, self.csv_di_text)
        # di_count = len(di_list)
        # print("count",di_count)
        # for lt in range(1,di_count):
        #     # listvalue = self.driver.find_element(By.XPATH,"//ul[@class='disc']//li")
        #     print(di_list.text)

    def upload(self):
        self.wait_until_element_is_clickable(By.XPATH, self.csv_di_upload).click()

    def verify_success_upload(self):
        suc =self.driver.find_element(By.XPATH,self.csv_di_up_success).text
        if "Number" in suc:
            print("successfully uploaded data")
