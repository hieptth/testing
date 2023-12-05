from xlrd import open_workbook # pip install xlrd ==1.2.0

def readDatafromExcel(sheetName):
    data = open_workbook("dataTesting.xlsx")
    sheet = data.sheet_by_name(sheetName)
    testcases = []
    for row_index in range(1, sheet.nrows):
        testcase = []
        for col_index in range(sheet.ncols):
            value = (sheet.cell(row_index,col_index).value)
            try:
                testcase.append(str(int(value)))
            except:
                testcase.append(str(value))

        testcases.append(testcase)
    return testcases

#print(readDatafromExcel('Login'))
        