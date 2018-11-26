# 98. Valid Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 解法一：对于节点root，遍历左子树返回最大值max，遍历右子树返回最大值min，验证max < root.val < min，然后递归调用root.left，root.right.
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

    # 解法二：运用dfs方法返回其中序遍历，检查是否严格递增
    def isValidBSTInOrder(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        order = []
        self.dfs(root, order)
        if order:
            if len(order) == 1:
                return True
            for i in range(len(order) - 1):
                if order[i] >= order[i + 1]:
                    return False

        return True

    def dfs(self, root, order):
        if not root:
            return

        self.dfs(root.left, order)
        order.append(root.val)
        self.dfs(root.right, order)