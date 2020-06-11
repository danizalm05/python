""""
Tic Tac Toe
https://techwithtim.net/tutorials/python-programming/tic-tac-toe-tutorial/
"""
board = [' ' for x in range(10)]  # This should be the first line in your program
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Insert  letter at the given position.
def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    #  returns True if that player has won.  bo = board   le = letter (O or X)
    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or   # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or   # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or   # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or   # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or   # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or   # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or   # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le))     # diagonal


def playerMove():
    pass


def selectRandom(li):
    pass


def compMove():
    pass


def isBoardFull(board):
    if board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
             # There is at least one empty cell
        return False
    else:   # If only one cell is empty the board is full
        return True


def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def main():
    printBoard(board)

main()