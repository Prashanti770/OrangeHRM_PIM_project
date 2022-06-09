import pytest
from pageobjects.PIM import OH_PIM_EmployeeList
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_007_PIM_Delete_Emp(Test_002_OH_PIM_EmpList):

    def test_delete_empinfo(self):
        self.logger.info("*************** Test_007_PIM_Delete_Emp *****************")
        self.dei = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Employee Info Delete based on empid *****************")
        empid = "0204"
        self.dei.empinfo_emp_delete(empid)
        self.logger.info("*************** Delete popup confirmation message *****************")
        self.dei.del_conf_msg()
        #self.logger.info("*************** Delete popup cancel  *****************")
        # self.dei.del_cancel()
        # self.logger.info("*************** Delete popup close *****************")
        # self.dei.del_close()
        self.logger.info("*************** delete popup ok  *****************")
        self.dei.del_ok()
        self.logger.info("*************** delete success message *****************")
        self.dei.cnf_del_success()
