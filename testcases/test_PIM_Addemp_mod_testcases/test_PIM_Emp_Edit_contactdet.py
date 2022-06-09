import time

import pytest
from pageobjects.PIM.OH_PIM_Contactdetails import OH_PIM_Contactdetails
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM.OH_PIM_EmployeeList import OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_012_PIM_Emp_Edit_Contactdetails(Test_002_OH_PIM_EmpList):

    def test_emp_contactdetails(self):
        self.logger.info("*************** Test_012_PIM_Emp_Edit_Contactdetails  *****************")
        self.pd = OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Click on Employee ID in EmpList table to Edit  employee info*****************")
        id ="0204"
        self.pd.table_link_click(id)
        self.logger.info("*************** click on contact details in Employee personal Information page  *****************")
        self.edit = OH_PIM_Contactdetails(self.driver)
        self.edit.click_contdetails()
        # self.logger.info("*************** Checking contact details are enabled or not *****************")
        # self.edit.contactdetails_verify()
        # self.logger.info("*************** clicking on Edit button in contact details *****************")
        # self.edit.edit_contdetails()
        # self.logger.info("*************** Filling the conatct details *****************")
        # self.edit.contdetails_fill("dsnr","hyd","TN","12349353450")
        self.logger.info("*************** Adding attachemnets in Contact Details *****************")
        choose_file = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\testing_file.txt"
        text = "testing process contact details"
        self.edit.contdetails_attach_add(choose_file,text)
        time.sleep(5)
        self.logger.info("***************  *****************")
        # self.edit.contdetails_attach_cancel()
        self.logger.info("***************  *****************")
        self.edit.contdetails_attach_upload()





