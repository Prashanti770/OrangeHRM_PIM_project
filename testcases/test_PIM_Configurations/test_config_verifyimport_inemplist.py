import csv

import pytest

from pageobjects.PIM import OH_PIM_EmployeeList
from testcases.test_PIM_Emplist_testcases.test_OH_PIM_EmpList import Test_002_OH_PIM_EmpList


@pytest.mark.usefixtures("test_OH_pim")
class Test_config_verifyimport(Test_002_OH_PIM_EmpList):

    def test_verifyimport(self):
        self.logger.info("*************** Searching Employee Info *****************")
        self.logger.info("*************** Employee Info - Search by Employee id *****************")
        self.empid = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        filepath_1 = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\importData.csv"
        filedata = open(filepath_1, "r")
        # to read data from csv file
        reader = csv.reader(filedata)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count+=1

            else:
                print(row[3])
                self.empid.empinfo_empid(row[3])
                self.empid.empinfo_search()
                self.empid.table_searchempbyId(row[3])
                line_count += 1

        # self.empid = OH_PIM_EmployeeList.OH_PIM_EmpList(self.driver)
        # self.empid.empinfo_empid(emp_id)
