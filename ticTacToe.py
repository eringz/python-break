# Print the board 3 x 3
# Make a condition for turning X and 0 alternatively with respective board loacation


theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def printBoard(board):
    print('%s|%s|%s' % (board['top-L'], board['top-M'], board['top-R']))
    print('-+-+-')
    print('%s|%s|%s' % (board['mid-L'], board['mid-M'], board['mid-R']))
    print('-+-+-')
    print('%s|%s|%s' % (board['low-L'], board['low-M'], board['low-R']))


printBoard(theBoard)

turn = 'X'
for i in range(9):
    move = input('Make a move?: ')
    theBoard[move] = turn
    printBoard(theBoard)
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

