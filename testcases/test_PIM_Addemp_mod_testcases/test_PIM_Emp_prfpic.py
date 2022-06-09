import time

import pytest
from pageobjects.PIM.OH_PIM_Personaldetails import OH_PIM_Emp_Perdetails
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM.OH_PIM_EmployeeList import OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_010_PIM_Emp_Prfpic(Test_002_OH_PIM_EmpList):

    def test_emp_attachments(self):
        self.pd = OH_PIM_EmpList(self.driver)
        id ="0204"
        self.pd.table_link_click(id)
        self.edit = OH_PIM_Emp_Perdetails(self.driver)
        self.logger.info("*************** Employee Profile picture edit *****************")
        choose_file = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\emp1.png"
        self.edit.edit_emp_pic()
        self.logger.info("*************** Employee Profile picture upload *****************")
        # self.edit.edit_emppic_upload(choose_file)
        self.logger.info("*************** Employee Profile picture delete *****************")
        self.edit.edit_emppic_delete()
        self.logger.info("*************** Employee Profile picture delete popup*****************")
        self.edit.del_popup_ok()
        self.edit.cnf_del_success()
        # self.edit.del_close()
        # time.sleep(5)
        # self.edit.del_cancel()





