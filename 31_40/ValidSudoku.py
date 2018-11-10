class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict = {}
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

    def conflict(self, list, pos):
        valid = False
        for other in list:
            if other[0] == pos[0] or other[1] == pos[1]:
                return True
            elif other[0]//3 == pos[0]//3 and other[1]//3 == pos[1]//3:
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
                    for k in range(9):
                        board[i][j] = str(k)
                        if self.isValidSudoku(board) and self.solveSudoku(board):
                            return True
                        board[i][j] = "."
                    return False

        return False

    def isValid(self, board, x, y):
        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Solution().solveSudoku(board)
print(board)