import time

import pytest
from pageobjects.PIM.OH_PIM_Contactdetails import OH_PIM_Contactdetails
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList
from pageobjects.PIM.OH_PIM_EmployeeList import OH_PIM_EmpList

@pytest.mark.usefixtures("test_OH_pim")
class Test_013_PIM_Emp_Edit_Emergencycntct(Test_002_OH_PIM_EmpList):

    def test_emp_contactdetails(self):
        self.logger.info("*************** Test_012_PIM_Emp_Edit_Contactdetails  *****************")
        self.pd = OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Click on Employee ID in EmpList table to Edit  employee info*****************")
        id ="0204"
        self.pd.table_link_click(id)
        self.logger.info("*************** click on contact details in Employee personal Information page  *****************")
        self.edit = OH_PIM_Contactdetails(self.driver)
        self.edit.emgncy_contdetails()
        self.logger.info("*************** clicking on Add button in Emergency contact details *****************")
        self.edit.emg_cont_add("sha","sis","980")
        self.edit.emg_cont_save()

        self.logger.info("*************** Adding attachemnets in Emergency contact Details *****************")
        choose_file = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\testing_file.txt"
        text = "testing process emergency contact details"
        self.edit.contdetails_attach_add(choose_file,text)
        time.sleep(5)
        self.logger.info("***************  *****************")
        # self.edit.contdetails_attach_cancel()
        self.logger.info("***************  *****************")
        self.edit.contdetails_attach_upload()





