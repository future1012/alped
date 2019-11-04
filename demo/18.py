spam = ['pear', 'apples', 'bananas', 'tofu', 'cats','abc','111','222']
for i in spam:
    if spam.index(i) == len(spam) - 1:
        i = 'and ' + i
        print(i, end='')
    else:
        print(i, end = ',')
