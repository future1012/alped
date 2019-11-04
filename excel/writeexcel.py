import xlwt
#https://www.cnblogs.com/nancyzhu/p/8401552.html
students = [
    ['姓名','年龄','性别','分数'],
    ['mary',20,'女',89.9],
    ['mary',20,'女',89.9],
    ['mary',20,'女',89.9],
    ['mary',20,'女',90.9],
]

def write_excel(data,filename):
    #新建一个excel对象
    book = xlwt.Workbook()
    # 给这个book添加一个sheet
    sheet = book.add_sheet('info')
    row = 0
    for stu in data:
        col = 0
        for i in stu:
            #给指定单元格写入数据
            sheet.write(row,col, i)
            col += 1
        row += 1
    #保存写入的数据到文件
    book.save(filename)

if __name__ == '__main__':
    write_excel(students, 'aaa.xls')

