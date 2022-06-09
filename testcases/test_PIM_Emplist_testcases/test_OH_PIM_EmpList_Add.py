import allure
import pytest
from testcases.test_PIM_Emplist_testcases import test_OH_PIM_addemp_details
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList


@pytest.mark.usefixtures("test_OH_pim")
@allure.severity(allure.severity_level.NORMAL)
class Test_005_OH_PIM_EmpList_Add(Test_002_OH_PIM_EmpList):
    addemp_details = test_OH_PIM_addemp_details.Test_PIM_addemp_details

    @allure.severity(allure.severity_level.CRITICAL)
    def test_emplist_addbtn(self):
        self.logger.info("*************** Test_005_OH_PIM_EmpList_Add  *****************")
        self.logger.info("*************** Clicking on Add Employee *****************")
        self.OH_pim_empinfo.empinfo_add()
        self.logger.info("*************** Adding Employee Details *****************")
        self.addemp_details.test_addemployee(self)
        self.addemp_details.test_createlogin(self)
        self.addemp_details.test_empdetails_save(self)






