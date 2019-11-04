theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printBorad(board):
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

turn = 'X'
for i in range(9):
    printBorad(theBoard)
    move = input('plz move: ')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBorad(theBoard)
