class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dict = self.buildDict(board)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        board[i][j] = str(k)
                        if board[i][j] in dict.keys():
                            list = dict[board[i][j]]
                        else:
                            list = []
                        if not self.conflict(list, [i, j]) and self.solveSudoku(board):
                            return True
                        board[i][j] = "."
                    return False
        return True

    def conflict(self, list, pos):
        valid = False
        for other in list:
            if other[0] == pos[0] or other[1] == pos[1]:
                return True
            elif other[0]//3 == pos[0]//3 and other[1]//3 == pos[1]//3:
                return True

        return valid

    def buildDict(self, board):
        dict = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in dict.keys():
                        dict[board[i][j]] = [[i, j]]
                    else:
                        dict[board[i][j]].append([i, j])

        return dict


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