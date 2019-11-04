name_and_bthd = {'xiaoming': '1023', 'xiaohong': '1112', 'xiaogang': '1212'}
print('welcome!')
while True:
    name = input('plz input a name: ')
    if name == '':
        break
    if name in name_and_bthd:
        print(name_and_bthd[name] + ' is the birthday of '+name)
        print(name_and_bthd)
    else:
        print('I do not have birthday info for ' + name)
        unknowname = input('which day is  ' + name + '\' birthday? ')
        name_and_bthd[name]=unknowname
        print('databases is updated')
        print(name_and_bthd)
        print(name_and_bthd[name] + ' is ' + name + '\'s birthday!')
