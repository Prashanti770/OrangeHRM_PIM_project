import pytest

from pageobjects.PIM import OH_PIM_EmployeeList, OH_PIM_Config_OptFields
from testcases.test_OH_loginpage import Test_001_OH_Login
from pageobjects.PIM import OH_PIM_Config_Custfields


@pytest.mark.usefixtures("test_OH_loginpage")
class Test_OH_PIM_Config_CF(Test_001_OH_Login):

    def test_config_opf(self):
        self.logger.info("*************** Test_OH_PIM_EmpList *****************")
        self.OH_pim_empinfo = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        self.logger.info("*************** Clicking on PIM Module *****************")
        self.OH_pim_empinfo.oh_pim()
        self.logger.info("*************** Clicking on Configurations Module *****************")
        self.pim_conf= OH_PIM_Config_OptFields.OH_PIM_Configuration(self.driver)
        self.pim_conf.configuration()
        self.logger.info("*************** Clicking on Custom Fields Module *****************")
        self.pim_conf_cf = OH_PIM_Config_Custfields.OH_PIM_Configuration_CF(self.driver)
        self.pim_conf_cf.confg_customfields()
        # self.logger.info("*************** verifying count of Custom Fields Module *****************")
        # self.pim_conf_cf.dcf_verify_count()
        # self.logger.info("*************** Add Custom Fields  *****************")
        # self.pim_conf_cf.dcf_add()
        screen_value = "Memberships"
        type_value ="Text or Number"
        # self.pim_conf_cf.table_print()
        self.pim_conf_cf.dcf_table_search_del(screen_value,type_value)
