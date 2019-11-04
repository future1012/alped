from xlutils.copy import copy
import xlrd

#xlutils修改excel

#打开xls文件
book1 = xlrd.open_workbook('stu_1.xls')
#拷贝一份,
#注意这里不是用的xlrd包copy的
book2 = copy(book1)
# print(dir(book2))

#获取新拷贝的book的sheet
sheet = book2.get_sheet(0)

#将第二行第四列值改为0
sheet.write(1,3,0)
#将第二行第一列值改为hello
sheet.write(1,0,'hello')

#将写入的数据保存到文件
book2.save('stu_2.xls')
