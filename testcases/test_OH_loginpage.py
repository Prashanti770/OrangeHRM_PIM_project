import time
import allure
import pytest
from allure_commons.types import AttachmentType
from pageobjects.OH_loginpage import OH_Loginpage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

@allure.severity(allure.severity_level.BLOCKER)
class Test_001_OH_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loginfo()

    @pytest.fixture
    @pytest.mark.sanity
   # @allure.severity(allure.severity_level.CRITICAL)
    def test_OH_loginpage(self,setup):
        self.logger.info("*************** Test_001_OH_Login *****************")
        self.driver = setup
        self.logger.info("*************** openning Url ****************")
        self.driver.get(self.baseURL)
        self.logger.info("*************** Started Login page ****************")
        self.OH_lp = OH_Loginpage(self.driver)
        self.OH_lp.set_username(self.username)
        self.OH_lp.set_password(self.password)
        self.OH_lp.login_click()
        time.sleep(3)

        act_welcome_text = self.OH_lp.welcome_msg()
        exp_welcome_text = "Welcome "
        if exp_welcome_text in act_welcome_text :
            self.logger.info("*************** Login successfull ****************")
            allure.attach(self.driver.get_screenshot_as_png(), name="Test_001_OH_Login_success", attachment_type=AttachmentType.PNG)
            # self.OH_lp.logout_click()
            assert True
        else :
            self.logger.error("*************** Login Failed ****************")
            allure.attach(self.driver.get_screenshot_as_png(), name="Test_001_OH_Login_fail",
                          attachment_type=AttachmentType.PNG)
            assert False





