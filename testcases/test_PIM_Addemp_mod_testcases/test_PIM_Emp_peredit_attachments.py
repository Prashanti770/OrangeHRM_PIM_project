import pytest
from pageobjects.PIM.OH_PIM_Personaldetails import OH_PIM_Emp_Perdetails
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM.OH_PIM_EmployeeList import OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_PIM_emp_edit_attch(Test_002_OH_PIM_EmpList):

    def test_emp_attachments(self):
        self.pd = OH_PIM_EmpList(self.driver)
        id ="0204"
        self.pd.table_link_click(id)
        self.edit = OH_PIM_Emp_Perdetails(self.driver)
        self.logger.info("*************** changing value in Attachments *****************")
        choose_file = "C:\\PrashantiM\\OrangeHRM_project-master\\testdata\\testing_file.txt"
        text = "testing process"
        self.edit.edit_attachments(choose_file,text)



