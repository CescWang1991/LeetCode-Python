# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: Tree
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        dist = abs(root.val - target)
        if target < root.val:
            left = self.closestValue(root.left, target)
            if left and dist < abs(left - target):
                return root.val
            else:               # 不存在左子树或者差值小于左子树返回的差值
                return left
        if target > root.val:
            right = self.closestValue(root.right, target)
            if right and dist < abs(right - target):
                return root.val
            else:               # 不存在右子树或者差值小于右子树返回的差值
                return right