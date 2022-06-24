import time

import pytest

from pageobjects.PIM import OH_PIM_EmployeeList, OH_PIM_Config_OptFields
from testcases.test_OH_loginpage import Test_001_OH_Login
from pageobjects.PIM import OH_PIM_Config_Custfields


@pytest.mark.usefixtures("test_OH_loginpage")
class Test_OH_PIM_Config_CF(Test_001_OH_Login):
    name = "OTT"
    screen_value = "Memberships"
    type_value = "Text or Number"

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
        self.logger.info("*************** verifying count of Custom Fields Module *****************")
        self.pim_conf_cf.dcf_verify_count()
        self.logger.info("*************** Add Custom Fields button click *****************")
        self.pim_conf_cf.dcf_add()
        self.logger.info("*************** Adding values in Custom Fields  *****************")
        self.pim_conf_cf.dcf_addvalues(self.name,self.screen_value,self.type_value)
        self.logger.info("*************** Save added values in Custom Fields  *****************")
        self.pim_conf_cf.acf_save()
        # self.logger.info("*************** Cancel adding in Custom Fields  *****************")
        # self.pim_conf_cf.acf_cancel()
        self.logger.info("*************** verifying count of Custom Fields Module after adding *****************")
        self.pim_conf_cf.dcf_verify_count()
        # self.logger.info("*************** Print table of custom fields  *****************")
        # self.pim_conf_cf.table_print()
        # self.logger.info("*************** Click on Delete button in Custom Fields *****************")
        # self.pim_conf_cf.dcf_table_search_delete(self.name)
        # time.sleep(3)
        # self.logger.info("*************** Click on ok in Delete popup *****************")
        # self.pim_conf_cf.del_ok()
        # self.logger.info("*************** verifying count of Custom Fields Module after deleting *****************")
        # self.pim_conf_cf.dcf_verify_count()
        # self.logger.info("*************** Click on cancel in Delete popup *****************")
        # self.pim_conf_cf.del_cancel()
        # self.logger.info("*************** Click on close in Delete popup *****************")
        # self.pim_conf_cf.del_close()

