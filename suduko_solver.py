def printBoard(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()


def checkBoard(board) -> bool:
    for row in range(9):
        for col in range(9):
            if testSafe(board, row, col, board[row][col]) == False:
                return False
    return True


def testSafe(board, row: int, col: int, num: int) -> bool:
    testBoard = board[:]
    testBoard[row][col] = num

    columnList = [testBoard[i][col] for i in range(9)]
    box = []
    for i in range( int(row / 3) * 3, int(row / 3 + 1) * 3 ):
        box += testBoard[i][int(col / 3) * 3: int(col / 3 + 1) * 3]

    for number in range(1,10):
        if testBoard[row].count(number) > 1:
            return False
        if columnList.count(number) > 1:
            return False
        if box.count(number) > 1:
            return False
    
    return True


def findEmpty(board, l):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                l[0] = i
                l[1] = j
                return True
    return False


def solve(board):
    """main function to solve the board, stores the solved board in solvedBoard"""
    if not checkBoard(board):
        print("board invalid")
        return False
    
    l = [0,0]
    if not findEmpty(board, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if testSafe(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            
        board[row][col] = 0
    
    return False


"""
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]
"""


grid = [[0, 9, 0, 2, 0, 3, 0, 4, 0],
        [4, 0, 7, 0, 9, 0, 8, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 9, 0],
        [3, 0, 0, 6, 0, 5, 0, 0, 9],
        [0, 4, 0, 0, 1, 0, 0, 2, 0],
        [5, 0, 0, 9, 0, 4, 0, 0, 3],
        [0, 2, 0, 0, 0, 0, 0, 8, 0],
        [1, 0, 3, 0, 6, 0, 2, 0, 4],
        [0, 6, 0, 4, 0, 2, 0, 3, 0]]


solve(grid)

printBoard(grid)
