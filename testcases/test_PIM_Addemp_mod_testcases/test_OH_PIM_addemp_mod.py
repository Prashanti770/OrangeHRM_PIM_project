import time

import allure
import pytest
from testcases.test_OH_loginpage import Test_001_OH_Login
from pageobjects.PIM import OH_PIM_EmployeeList
from pageobjects.PIM import OH_PIM_EmpList_Add
from testcases.test_PIM_Emplist_testcases import test_OH_PIM_addemp_details

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_OH_loginpage")
@pytest.mark.sanity
class Test_006_OH_PIM_EmpList_Add(Test_001_OH_Login):
    addemp_details = test_OH_PIM_addemp_details.Test_PIM_addemp_details

    @allure.severity(allure.severity_level.NORMAL)
    def test_addemp_mod(self):
        self.logger.info("*************** Test_006_OH_PIM_EmpList_Add Employee  *****************")
        self.logger.info("*************** Clicking on PIM Module *****************")
        self.OH_pim_empinfo = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.OH_pim_empinfo.oh_pim()
        time.sleep(3)
        self.logger.info("*************** Clicking on Add Employee in PIM Module *****************")
        self.OH_pim_empinfo.oh_pim_addemp_mod()
        self.logger.info("*************** Adding Employee Details *****************")
        self.addemp_details.test_addemployee(self)
        # self.addemp_details.test_createlogin(self)
        self.addemp_details.test_empdetails_save(self)



