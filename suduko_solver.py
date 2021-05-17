from typing import List, NoReturn


def printBoard(board: List[List[int]]) -> NoReturn:
    """outputs the board in plaintext"""
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()


def checkBoard(board: List[List[int]]) -> bool:
    """checks wether the current entire board is valid"""
    for row in range(9):
        for col in range(9):
            if testSafe(board, row, col, board[row][col]) == False:
                return False
    return True


def testSafe(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """checks wether placing num at (row, col) is valid"""
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


def findEmpty(board: List[List[int]], pos: List[int]) -> bool:
    """finds the first empty (0) square, searches left-to-right, up-to-down, modifies pos in the process"""
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                pos[0] = i
                pos[1] = j
                return True
    return False


def solve(board: List[List[int]]) -> bool:
    """returns true or false depending on whether the board is solvable, modifies the board in the process"""
    if not checkBoard(board):
        return False
    
    pos = [0,0]
    if not findEmpty(board, pos):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1,10):
        if testSafe(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            
        board[row][col] = 0
    
    return False
