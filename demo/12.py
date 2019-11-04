tableData = [['apples', 'oranges', 'cherries', 'banana', 'aaaaaaaaaaa'],
             ['Alice', 'Bob', 'Carol', 'David', 'dfddfas'],
             ['dogs', 'cats', 'moose', 'goose', 'adsfasasasadfadsfas']]
def printTable():
    '''
    这是一个doc测试！！！
    :return:
    '''
    #计算每个内层列表项目的最大长度，并写进一个列表。
    maxlen_list = []
    for inner_list in tableData:
        each_len = []
        for i in inner_list:
            each_len.append(len(i))
        inner_list_max = max(each_len)
        maxlen_list.append(inner_list_max)
    #根据计算出来的每个内层列表长度的列表分配左右缩进的长度。
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j == 0:
                print(tableData[j][i].rjust(maxlen_list[j]) + ' ', end='')
            else:
                print(tableData[j][i].ljust(maxlen_list[j]) + ' ', end='')
        print('\n', end='')

if __name__ == '__main__':
    print(printTable.__doc__)
    printTable()
