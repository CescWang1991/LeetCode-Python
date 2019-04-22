# 257. Binary Tree Paths

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.dfs(root, "")
        return self.res

    def dfs(self, root, path):
        if not root:
            return
        if not path:
            path += str(root.val)
        else:
            path += "->" + str(root.val)
        if not root.left and not root.right:    # 对于叶节点，将path加入到res中
            self.res.append(path)
        self.dfs(root.left, path)
        self.dfs(root.right, path)