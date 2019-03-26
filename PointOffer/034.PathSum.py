# 二叉树中和为某一值的路径

# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经
# 过的结点形成一条路径。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findPath(self, root, sum):
        if not root:
            return []
        self.result = []
        self.dfs(root, sum, [])
        return self.result

    def dfs(self, curr, sum, path):
        if not curr:
            return
        path.append(curr.val)
        if not curr.left and not curr.right:
            if curr.val == sum:
                self.result.append(path)
            return
        self.dfs(curr.left, sum - curr.val, path)
        self.dfs(curr.right, sum - curr.val, path)

        return
