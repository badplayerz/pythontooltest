import math

import openpyxl



excel_file = openpyxl.load_workbook('./resource_exc/otherside_bayc_leak.xlsx')

sheet = excel_file['Sheet1']
num = sheet.max_row

print(str(num))
m = 1
for i in range(1,num):
    cell = sheet['A' + str(i)]
    value1 = int(cell.value)+1
    # if m != int(cell.value)+1:
    #     print('%d,%d',m,int(cell.value)-1)
    #     m = m+1
    # m = m + 1

    x = int(math.fabs(m - value1))

    if x >= 1:
        for n in range(1,x+1):
            print(int(value1-1 - n))
        m = value1

    m = m+1

