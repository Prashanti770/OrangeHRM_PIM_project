import pytest

from pageobjects.OH_Time_Excel_Timesheet import Excel_Time
from testcases.test_OH_loginpage import Test_001_OH_Login

@pytest.mark.usefixtures("test_OH_loginpage")
class Test_Time_excel(Test_001_OH_Login):

    def test_excel_time(self):
        self.T =Excel_Time(self.driver)
        self.T.timesheet()

        self.T.excel_timedata()  # ,mon,tue,wed,thu,fri
