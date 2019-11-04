from excel import writeexcel

stu = [
    ['姓名','年龄','性别','分数'],
    ['mary',21,'女',89.9],
    ['mary',20,'女',89.9],
    ['mary',20,'女',89.9],
    ['mary',20,'女',89.9],
]
writeexcel.write_excel(stu, 'abc.xls')