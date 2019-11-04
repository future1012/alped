import xlrd

#只读

#打开一个execl文件
book = xlrd.open_workbook('stu_1.xls')

#利用索引获取一个sheet
sheet = book.sheet_by_index(0)
print('sheet的类型是:', type(sheet))
print('打印sheet:', sheet)

#获取sheet名字
print('sheet的名字是: {0}'.format(book.sheet_names()))

#利用sheet的名字获取此sheet
sheet1 = book.sheet_by_name('info')


#获取sheet中单元格的数据行数和列数索引是参数.
v00 = sheet.cell(0,0)
v01 = sheet.cell(0,1)
print('aaa', type(v01))
# print(v01)
v00 = v00.value
print('aaa', type(v00))
print('第一行第一列数据是：{0}'.format(v00))
v01 = v01.value
print('第一行第二列数据是：{0}'.format(v01))
# print(type(v00))
# print(v00, v01)

#获取sheet的行数和列数
rows = sheet.nrows
cols = sheet.ncols
print('这个sheet一共{0}行，{1}列'.format(rows,cols))

#获取sheet每行数据(是个生成器)
grows = sheet.get_rows()
print(type(sheet.get_rows()))
print('利用生成器for循环出sheet数据:')
for i in grows:
    print(i)
print('-'*20)
#获取指定行的值
print('这个sheet的第一行数据是：{0}'.format(sheet.row_values(0)))
print('这个sheet的第一列数据是：{0}'.format(sheet.col_values(0)))
print()
print('利用row_values()方法for循环打印sheet数据: ')
for i in range(rows):
    print(sheet.row_values(i))