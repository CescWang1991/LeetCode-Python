# 110. Balanced Binary Tree
# 运用Bottom-up方法，辅助函数dfsHeight返回树的高度，如果左右子树高度差大于1，或者左右子树有一个不平衡，则返回-1。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if not root:
            return 0

        left = self.dfsHeight(root.left)
        if left == -1:
            return -1
        right = self.dfsHeight(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1