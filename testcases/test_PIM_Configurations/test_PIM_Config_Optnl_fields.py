import pytest

from pageobjects.PIM import OH_PIM_EmployeeList
from testcases.test_OH_loginpage import Test_001_OH_Login
from pageobjects.PIM import OH_PIM_Config_OptFields


@pytest.mark.usefixtures("test_OH_loginpage")
class Test_OH_PIM_Config_OPF(Test_001_OH_Login):

    def test_config_opf(self):
        self.logger.info("*************** Test_OH_PIM_EmpList *****************")
        self.OH_pim_empinfo = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Clicking on PIM Module *****************")
        self.OH_pim_empinfo.oh_pim()
        self.logger.info("*************** Clicking on Configurations Module *****************")
        self.pim_conf_opf = OH_PIM_Config_OptFields.OH_PIM_Configuration(self.driver)
        self.pim_conf_opf.configuration()
        self.logger.info("*************** Clicking on Operational Fields Module *****************")
        self.pim_conf_opf.optional_fields()
        self.logger.info("*************** Verifying Configure PIM *****************")
        self.pim_conf_opf.configure_PIM_verify()
        self.logger.info("*************** Click Edit Configure PIM *****************")
        self.pim_conf_opf.config_opf_edit()
        self.logger.info("*************** Editing Configure PIM *****************")
        self.pim_conf_opf.config_opf_check()
        self.logger.info("*************** Save Configure PIM *****************")
        self.pim_conf_opf.config_opf_edit()
        self.logger.info("*************** Verifying Configure PIM after modify *****************")
        self.pim_conf_opf.configure_PIM_verify()



