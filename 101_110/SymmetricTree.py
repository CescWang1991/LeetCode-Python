# 101. Symmetric Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, p ,q):
        if not p:
            return not q
        if not q:
            return False

        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)