import time
import pytest
from pageobjects.PIM import OH_PIM_EmployeeList, OH_PIM_Config_OptFields
from pageobjects.PIM.OH_PIM_DataImport import OH_PIM_Configuration_DI
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
        self.logger.info("*************** Clicking on Data Import in Configurations Module *****************")
        self.pim_conf_di = OH_PIM_Configuration_DI(self.driver)
        self.pim_conf_di.dataimport()
        # self.logger.info("*************** Capturing instructions text in Data Import *****************")
        # self.pim_conf_di.csvdi_text()
        # self.logger.info("*************** Downloading sample csv file in Data Import *****************")
        # self.pim_conf_di.csvfile_dwnld()
        self.logger.info("*************** selecting CSV for upload in Data Import *****************")
        filepath = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\importData.csv"
        self.pim_conf_di.file_choose(filepath)
        self.logger.info("*************** click on upload button in Data Import *****************")
        self.pim_conf_di.upload()
        self.logger.info("*************** Verify successfull upload in Data Import *****************")
        self.pim_conf_di.verify_success_upload()




