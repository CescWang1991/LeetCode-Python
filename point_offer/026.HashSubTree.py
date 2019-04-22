# 026. 树的子结构

# 输入两棵二叉树A和B，判断B是不是A的子结构。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasSubTree(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val == b.val:
            if self.hasSubTree(a.left, b.left) and self.hasSubTree(a.right, b.right):
                return True

        return self.hasSubTree(a.left, b) or self.hasSubTree(a.right, b)