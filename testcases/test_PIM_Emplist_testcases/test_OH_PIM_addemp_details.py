import allure
from allure_commons.types import AttachmentType

from pageobjects.PIM import OH_PIM_EmpList_Add


@allure.severity(allure.severity_level.NORMAL)
class Test_PIM_addemp_details:

    @allure.severity(allure.severity_level.NORMAL)
    def test_addemployee(self):
        self.logger.info("*************** Test Method : Test_PIM_addemp_details  *****************")
        self.logger.info("*************** Adding Employee *****************")
        first = "orange2"
        middle = "hrm1"
        last = "demo1"
        # path_photo = "C:\\Users\\User\\Downloads\\R.png"
        path_photo = "C:\\PrashantiM\\OrangeHRM_project-master\\testdata\\R.png"
        self.add_emp = OH_PIM_EmpList_Add.OH_PIM_EmpList_Add(self.driver)
        self.add_emp.emplist_addemp(first ,middle ,last ,path_photo)
        self.logger.info("*************** Clicking on Creating Login option *****************")
        username = "ora123"
        password = "Test@0987"
        con_pwd = "Test@0987"
        status = "Disabled"
        self.add_emp.addemp_createlogin_btn(username ,password ,con_pwd ,status)
        allure.attach(self.driver.get_screenshot_as_png(), name="Test_PIM_addemp_details", attachment_type=AttachmentType.PNG)
        self.logger.info("*************** Clicking on save button *****************")
        self.add_emp.addemp_savebtn()

