import pytest
from pageobjects.PIM import OH_PIM_EmployeeList
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_PIM_delete_emp(Test_002_OH_PIM_EmpList):

    def test_delete_empinfo(self):
        self.dei = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        empid = "0204"
        self.dei.empinfo_emp_delete(empid)
        self.dei.del_conf_msg()
        # self.dei.del_cancel()
        # self.dei.del_close()
        self.dei.del_ok()
        self.dei.cnf_del_success()
