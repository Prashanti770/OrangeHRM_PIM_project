import time
import allure
import pytest
from testcases.test_OH_loginpage import Test_001_OH_Login
from pageobjects.PIM import OH_PIM_EmployeeList

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("test_OH_loginpage")
class Test_002_OH_PIM_EmpList(Test_001_OH_Login):

    @pytest.fixture(scope="function")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_OH_pim(self):
        self.logger.info("*************** Test_002_OH_PIM_EmpList *****************")
        self.OH_pim_empinfo = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Clicking on PIM Module *****************")
        self.OH_pim_empinfo.oh_pim()
        self.logger.info("*************** Clicking on Employee List in PIM Module *****************")
        self.OH_pim_empinfo.oh_pim_emplist()

    # def test_empinfo_searchbyname(self):
    #     self.test_OH_pim()
    #     self.logger.info("*************** Searching Employee Info *****************")
    #     empname = "Goutam Ganesh"
    #     self.logger.info("*************** Employee Info - Search by Employee name *****************")
    #     self.OH_pim_empinfo.empinfo_empname(empname)  # not giving input
    #     self.logger.info("*************** Employee Info - Search button click *****************")
    #     self.OH_pim_empinfo.empinfo_search()

    #     supvname = "Odis"
    #
        # self.logger.info("*************** Employee Info - Search by Employement status *****************")
        # self.OH_pim_empinfo.empinfo_empstatus()
    #     self.logger.info("*************** Employee Info - Search by Include *****************")
    #     self.OH_pim_empinfo.empinfo_include()
    #     self.logger.info("*************** Employee Info - Search by supervisor name *****************")
    #     self.OH_pim_empinfo.empinfo_supervisorname(supvname)
    #     self.logger.info("*************** Employee Info - Search by Jobtitle *****************")
    #     self.OH_pim_empinfo.empinfo_jobtitle("QA Engineer")
    #     self.logger.info("*************** Employee Info - Search by Subunit *****************")
    #     self.OH_pim_empinfo.empifno_subunit()
    #     self.logger.info("*************** Employee Info - Search button click *****************")
    #     self.OH_pim_empinfo.empinfo_search()
    #     time.sleep(5)
    #     self.logger.info("*************** Employee Info - reset button click *****************")
    #     self.OH_pim_empinfo.empinfo_reset()
    #
    #
    #
    #
