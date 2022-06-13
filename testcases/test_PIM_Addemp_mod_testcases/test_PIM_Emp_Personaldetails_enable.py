import pytest
from pageobjects.PIM.OH_PIM_Personaldetails import OH_PIM_Emp_Perdetails
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM.OH_PIM_EmployeeList import OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_009_PIM_Emp_Perdetails(Test_002_OH_PIM_EmpList):

    def test_emp_perdetails(self):
        self.pd = OH_PIM_EmpList(self.driver)
        id ="0204"
        self.pd.table_link_click(id)
        self.edit = OH_PIM_Emp_Perdetails(self.driver)
        # self.logger.info("*************** verify Employee Personal Details enable or not *****************")
        self.edit.personaldetails_verify()
        # self.logger.info("*************** Clicking on Edit in Personal Details *****************")
        # self.edit.edit_pd()

        #verify text box
        # self.edit.verify_textbox()

        # self.logger.info("*************** verify Employee Personal Details enable or not *****************")
        # self.edit.personaldetails_verify()
        # self.logger.info("*************** changing value in Personal Details *****************")
        # nation_name = "Indian"
        # radio = "M"
        # self.edit.edit_pdetails(nation_name,radio)
        # self.edit.edit_calendar("2022-09-10")
        # self.edit.save_pd()
        # self.logger.info("*************** changing value in custom fields *****************")
        # cfvalue = "A+"
        # self.edit.edit_cfields(cfvalue)


