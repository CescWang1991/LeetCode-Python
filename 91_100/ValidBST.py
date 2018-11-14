# 98. Valid Binary Search Tree
# 对于节点root，遍历左子树返回最大值max，遍历右子树返回最大值min，验证max < root.val < min，然后递归调用root.left，root.right.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isValidBST(root.left) and self.isValidBST(root.right) and self.maxValueInTree(root.left) < root.val < self.minValueInTree(root.right)

    def maxValueInTree(self, root):
        max = -1
        while root:
            max = root.val
            root = root.right

        return max

    def minValueInTree(self, root):
        min = int("inf")
        while root:
            min = root.val
            root = root.left

        return min