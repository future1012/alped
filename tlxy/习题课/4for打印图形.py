'''
打印如下图形:
* * * * *
*       *
*       *
* * * * *
'''

for i in range(4):
    if i==0 or i ==3:
        print('* '*5)
    else:
        print('*'+' '*7 + '*')

'''
打印如下图形：
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,6):
    print('* '*i)

''' 
打印如下图形：
*
* *
*   *
*     *
* * * * *
'''
for i in range(5):
    for j in range(i+1):
        if i == 4:
            print('* ',end='')
            continue
        if j==0 or j==i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()

'''
打印如下图形：
* * * * *
* * * *
* * *
* *
*
'''
print('###')
for i in range(5):
    for j in range(5-i):
        print('* ',end='')
    print()
print('###')
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('* ',end='')
    print()

'''
打印如下图形：
* * * * *
*     * 
*   *
* *
*
'''
print('###')
for i in range(5):
    for j in range(5-i):
        if i == 0:
            print('* ',end='')
            continue
        if j == 0 or j == 4-i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()

'''
打印正三角形：
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for m in range(i+1):
        print('* ',end='')
    print()

'''
打印空正三角：
    *      m=1   i=0 j=5
   * *     m=2   i=1 j=4
  *   *    m=3 6 i=2 j=3
 *     *   m=4 7 i=3 j=2
* * * * *
7 
     *         5
    *  7       4
   *    8      3
  *      9     2
 * * * * * 10  1
'''
print('###')
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for m in range(i+1):
        if i == 4:
            print('* ',end='')
            continue
        if m == 0 or m == i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
