import time
import allure
import pytest
from allure_commons.types import AttachmentType

from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM import OH_PIM_EmployeeList

@pytest.mark.usefixtures("test_OH_pim")
@allure.severity(allure.severity_level.NORMAL)
class Test_004_OH_PIM_Empinfo_Searchbyid(Test_002_OH_PIM_EmpList):

    # @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_empinfo_searchbyid(self):
        self.logger.info("*************** Searching Employee Info *****************")
        self.logger.info("*************** Employee Info - Search by Employee id *****************")
        emp_id = "0208"
        self.empid = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.empid.empinfo_empid(emp_id)
        self.logger.info("*************** Employee Info - Search button click *****************")
        self.empid.empinfo_search()
        self.logger.info("*************** Employee Info - Verify in table results *****************")
        allure.attach(self.driver.get_screenshot_as_png(), name="Test_004_OH_PIM_Empinfo_Searchbyid", attachment_type=AttachmentType.PNG)
        self.empid.table_searchempbyId(emp_id)
        # self.empid.table_link_click(emp_id)
        # status = self.empid.searchempbyId(empid)
        # assert True == status
        # print(status)






