import time
import allure
import pytest
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM import OH_PIM_EmployeeList


@pytest.mark.usefixtures("test_OH_pim")
@allure.severity(allure.severity_level.NORMAL)
class Test_003_OH_PIM_Empinfo_SearchbyName(Test_002_OH_PIM_EmpList):

    @allure.severity(allure.severity_level.NORMAL)
    def test_pim_searchbyname(self):
        empname = "Goutam Ganesh"
        self.empname = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Employee Info - Search by Employee name *****************")
        self.empname.empinfo_empname(empname)
        self.logger.info("*************** Employee Info - Search button click *****************")
        self.empname.empinfo_search()

