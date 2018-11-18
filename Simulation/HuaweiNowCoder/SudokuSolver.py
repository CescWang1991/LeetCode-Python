# 数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，现在有一些简单的数独题目，请编写一个程序求解。
# LeetCode 37. Sudoku Solver

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    dict = {}
    valid = True
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != "0":
                if num not in dict.keys():
                    dict[num] = [(i, j)]
                else:
                    if conflict(dict[num], (i, j)):
                        return False
                    else:
                        dict[num].append((i, j))
    return valid


def conflict(list, pos):
    valid = False
    for other in list:
        if other[0] == pos[0] or other[1] == pos[1]:
            return True
        elif other[0] // 3 == pos[0] // 3 and other[1] // 3 == pos[1] // 3:
            return True

    return valid

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == "0":
                for k in range(1, 10):
                    board[i][j] = str(k)
                    if isValidSudoku(board) and solveSudoku(board):
                        return True
                    board[i][j] = "0"
                return False
    return True


while True:
    try:
        board = []
        for i in range(9):
            line = input()
            col = line.split(" ")
            board.append(col)
        solveSudoku(board)
        for col in board:
            for i in range(9):
                if i != 8:
                    print(int(col[i]), end=" ")
                else:
                    print(int(col[i]))
    except:
        break

board = [
    ['0', '9', '5', '0', '2', '0', '0', '6', '0'],
    ['0', '0', '7', '1', '0', '3', '9', '0', '2'],
    ['6', '0', '0', '0', '0', '5', '3', '0', '4'],
    ['0', '4', '0', '0', '1', '0', '6', '0', '7'],
    ['5', '0', '0', '2', '0', '7', '0', '0', '9'],
    ['7', '0', '3', '0', '9', '0', '0', '2', '0'],
    ['0', '0', '9', '8', '0', '0', '0', '0', '6'],
    ['8', '0', '6', '3', '0', '2', '1', '0', '5'],
    ['0', '5', '0', '0', '7', '0', '2', '8', '3']
]