from typing import List, NoReturn


def print_board(board: List[List[int]]) -> NoReturn:
    """outputs the board in plaintext"""
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()


def check_board(board: List[List[int]]) -> bool:
    """checks whether the current entire board is valid"""
    for row in range(9):
        for col in range(9):
            if not test_safe(board, row, col, board[row][col]):
                return False
    return True


def test_safe(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """checks whether placing num at (row, col) is valid"""
    test_board = board[:]
    test_board[row][col] = num

    column_list = [test_board[i][col] for i in range(9)]
    box = []
    for i in range(int(row / 3) * 3, int(row / 3 + 1) * 3):
        box += test_board[i][int(col / 3) * 3 : int(col / 3 + 1) * 3]

    for number in range(1, 10):
        if test_board[row].count(number) > 1:
            return False
        if column_list.count(number) > 1:
            return False
        if box.count(number) > 1:
            return False

    return True


def find_empty(board: List[List[int]], pos: List[int]) -> bool:
    """finds the first empty (0) square, searches left-to-right, up-to-down, modifies pos in the process"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                pos[0] = i
                pos[1] = j
                return True
    return False


def solve(board: List[List[int]]) -> bool:
    """returns true or false depending on whether the board is solvable, modifies the board in the process"""
    if not check_board(board):
        return False

    pos = [0, 0]
    if not find_empty(board, pos):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
        if test_safe(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True

        board[row][col] = 0

    return False
