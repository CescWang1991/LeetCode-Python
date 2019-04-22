# 114. Flatten Binary Tree to Linked List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 记录左子树与右子树
        left = root.left
        right = root.right
        # 当前节点的左子树设为None，右子树设为原来的左子树，然后对原左子树进行flatten递归调用
        root.left = None
        root.right = left
        self.flatten(left)
        # 原左子树铺平后，从根节点向右子节点遍历至叶节点，叶节点右子树设为原来的右子树
        while root and root.right:
            root = root.right
        # 对原右子树进行flatten递归调用
        root.right = right
        self.flatten(right)