import pytest
from pageobjects.PIM import OH_PIM_EmployeeList, OH_PIM_Config_OptFields
from pageobjects.PIM.OH_PIM_Config_Termination_Rsns import OH_PIM_Configuration_TR
from testcases.test_OH_loginpage import Test_001_OH_Login


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
        self.logger.info("*************** Clicking on Termination Reasons in Configurations Module *****************")
        self.pim_conf_tr = OH_PIM_Configuration_TR(self.driver)
        self.pim_conf_tr.termination_rsns()
        # self.logger.info("*************** Clicking on Add in Termination Reasons  *****************")
        # self.pim_conf_tr.ter_rsns_add()
        # self.logger.info("*************** Adding Name of Termination Reasons  *****************")
        # name = "no project"
        # self.pim_conf_tr.add_name(name)
        # self.logger.info("*************** Clicking on Save in Add - Termination Reasons  *****************")
        # self.pim_conf_tr.add_save()
        # self.logger.info("*************** Clicking on Cancel in Add -Termination Reasons  *****************")
        # self.pim_conf_tr.add_cancel()
        # self.logger.info("*************** Printing column values from table - Add in Termination Reasons  *****************")
        # self.pim_conf_tr.add_tr_table_print()
        # self.logger.info("*************** Deleting value from table -  Termination Reasons  *****************")
        # del_value = "Hemasri"
        # self.pim_conf_tr.tr_table_delete(del_value)
        # self.logger.info("*************** Printing column values from table -  Termination Reasons  *****************")
        # self.pim_conf_tr.tr_table()
        self.logger.info("*************** comparing add - table value and home table values in Termination Reasons  *****************")
        tr_table_values = self.pim_conf_tr.tr_table()
        self.pim_conf_tr.ter_rsns_add()
        add_table_values = self.pim_conf_tr.add_tr_table_print()
        t1 = set(add_table_values)
        t2 = set(tr_table_values)
        if t1==t2:
            print("two table values are same")
        else:
            print("two table values are not same")


