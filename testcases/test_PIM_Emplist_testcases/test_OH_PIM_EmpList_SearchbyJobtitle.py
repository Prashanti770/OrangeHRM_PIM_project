import allure
import pytest
from pageobjects.PIM import OH_PIM_EmployeeList
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
@allure.severity(allure.severity_level.NORMAL)
class Test_008_OH_PIM_Empinfo_Searchbyjobtitle(Test_002_OH_PIM_EmpList):

    @allure.severity(allure.severity_level.NORMAL)
    def test_empinfo_searchbyjobtitle(self):
        self.logger.info("*************** Searching Employee Info *****************")
        self.logger.info("*************** Employee Info - Search by Jobtitle *****************")
        # job_title = "Software Engineer"
        job_title = "HR Associate"
        self.jt = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.jt.empinfo_jobtitle(job_title)
        self.logger.info("*************** Employee Info - Search button click *****************")
        self.jt.empinfo_search()
        self.logger.info("*************** Employee Info - print table of search results in cmd based on jobtitle  *****************")
        self.jt.table_searchempbyId(job_title)
        # time.sleep(3)
        # self.logger.info("*************** Employee Info - delete employee based on job_title and emp id *****************")
        # emp_id = "0204"
        # self.jt.empinfo_emp_delete(emp_id)







