class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False
        seq = []
        valid = False
        for i in range(len(word)):
            res = self.search(board, word[i])
            if res:
                if not seq:
                    for pos in res:
                        seq.append([pos])
                else:
                    for pos in res:
                        for list in seq:
                            if len(list) == i and self.isValid(list, pos):
                                seq.append(list + [pos])

        for list in seq:
            if len(list) == len(word):
                valid = True

        return valid


    def search(self, board, target):
        m = len(board[0])
        n = len(board)
        result = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == target:
                    result.append((i, j))

        return result

    def isValid(self, seq, pos):
        valid = (abs(seq[-1][0] - pos[0]) + abs(seq[-1][1] - pos[1]) == 1)
        for p in seq:
            if p == pos:
                valid = False
        return valid


board = [
    ["a", "a", "a", "a"],
    ["a", "a", "a", "a"],
    ["a", "a", "a", "a"],
    ["a", "a", "a", "a"],
    ["a", "a", "a", "b"]
]
print(Solution().exist(board, "aaaaaaaaaaaaaaaaaaa"))