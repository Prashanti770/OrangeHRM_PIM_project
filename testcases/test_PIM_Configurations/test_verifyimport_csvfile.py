import  csv

class Test_verifyimport:

    def test_verify_di(self):
        filepath_1 = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\importData.csv"
        data = []
        #open csv file
        filedata = open(filepath_1,"r")
        #to read data from csv file
        reader = csv.reader(filedata)
        #To Remove Header
        # next(reader)

        # for rows in reader:
        #     # data.append(rows)
        #     print(rows[3])

        ##############################

        line_count = 0

        for row in reader:
            # print(len(row))
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

                # print("1st row data",row[3])
                line_count += 1

            else :
                # print(row)
                print("row data",row[3])
                data.append(row[3])
                line_count += 1
        print(data)
        filepath_2 = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\exportData.csv"
        filedata_2 = open(filepath_2, "w")
        export_write = csv.writer(filedata_2, delimiter=',')
        export_write.writerow(data)
        print("total lines in csv file",line_count)

################################################
    # filepath_2 = "C:\\PrashantiM\\OrangeHRM_PIM_project\\testdata\\exportData.csv"
    # filedata_2 = open(filepath_2, "w")
    # export_write = csv.writer(filedata_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # export_write.writerow()



