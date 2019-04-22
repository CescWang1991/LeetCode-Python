# 036. Valid Sudoku
# 037. Sudoku Solver

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict = {}   # hash表记录每个数字所在位置的列表
        valid = True
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num not in dict.keys():
                        dict[num] = [(i,j)]
                    else:
                        if self.conflict(dict[num], (i,j)):
                            return False
                        else:
                            dict[num].append((i,j))
        return valid
    # 判断当前的pos与其他相同的数的位置是否冲突
    def conflict(self, list, pos):
        valid = False
        for other in list:
            if other[0] == pos[0] or other[1] == pos[1]:    # 同行或同列
                return True
            elif other[0]//3 == pos[0]//3 and other[1]//3 == pos[1]//3: # 在一个九宫格内
                return True

        return valid

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        board[i][j] = str(k)
                        # 对于位置[i,j]，采用backtracking与dfs，填入1-9数字，如果当前出现冲突或者之后出现冲突
                        # 则将其重置为"."，并返回False，否则返回True。
                        if self.isValidSudoku(board) and self.solveSudoku(board):
                            return True
                        board[i][j] = "."
                    return False

        return True