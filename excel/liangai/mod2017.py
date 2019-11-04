from xlutils.copy import  copy
import xlrd

#打开一个excel文档，赋值给book，book是一个打开的excel对象
book = xlrd.open_workbook('2017.xlsx')

#利用xlutils.copy拷贝一份book为newbook
newbook = copy(book)

#用原始的book获取第一个sheet
orisheet = book.sheet_by_index(0)

#用拷贝的book获取一份sheet
sheet = newbook.get_sheet(0)

# 利用原始sheet获取sheet的行数和列数
rows = orisheet.nrows
cols = orisheet.ncols
print('这个sheet一共{0}行，{1}列'.format(rows,cols))
#

# 循环修改每一行的数据
for row in range(1,29996):
    #利用原始sheet获取指定单元格数据 .value
    celldata = orisheet.cell(row, 1).value
    # celldata是str类型，利用字符串方法replace替换指定字符串
    newdata = celldata.replace(celldata[6:],'*'* len(celldata[6:]))
    #利用拷贝的book里的sheet写入newdata到指定单元格
    sheet.write(row, 1, newdata)
    #保存写入sheet的数据
    newbook.save('new2017.xls')
    print('第{1}行，旧身份证信息：{2},新数据已经插入：{0}'.format(newdata,row,celldata))
