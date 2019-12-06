import openpyxl
import  os
print(os.getcwd())

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
sheetlist = wb.sheetnames
print(type(sheetlist))
sheet = wb['Sheet1']
#data = sheet['A1'].value
data = sheet['A1'].value
print(data)


