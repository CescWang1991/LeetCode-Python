# 212. Word Search II
# 与79. Word Search相似。

class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        # 建立字典树，将words中每一个word添加进去
        root = TrieNode()
        for word in words:
            node = root
            for letter in word:
                child = node.children.get(letter)
                if not child:
                    child = TrieNode()
                    node.children[letter] = child
                node = child
            node.isWord = True

        ans = []
        # 然后从地图board的每一个元素深度优先搜索
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(root, board, i, j, "", ans)

        return ans

    # 如果往上下左右搜索的时候其元素可以在字典树中找到, 那么就继续搜索下去
    def dfs(self, node, board, x, y, s, ans):
        letter = board[x][y]
        child = node.children.get(letter)
        # 如果在字典树中无法找到这个元素, 那么就结束当前分支的搜索。
        if not child or board[x][y] == "#":
            return
        s += board[x][y]
        # 并且如果搜索到某个结点的时候发现到这个结点构成了一个单词, 那么就将单词添加到结果集合中。
        if child.isWord:
            ans.append(s)
            child.isWord = False

        node = child
        row = len(board)
        col = len(board[0])

        # 标记搜索过的点, 可以改变其值, 搜索完之后再改回来
        board[x][y] = "#"
        if y > 0:           # 向左遍历
            self.dfs(node, board, x, y-1, s, ans)
        if y < col - 1:     # 向右遍历
            self.dfs(node, board, x, y+1, s, ans)
        if x > 0:           # 向上遍历
            self.dfs(node, board, x-1, y, s, ans)
        if x < row - 1:     # 向下遍历
            self.dfs(node, board, x+1, y, s, ans)

        board[x][y] = letter