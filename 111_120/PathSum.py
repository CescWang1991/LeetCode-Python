# 112. Path Sum
# 113. Path Sum II

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        # 当前节点为叶节点时，判断是否和剩余的sum相同
        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        lists = []
        # 对于叶节点，如果当前值等于剩余和，则将当前值加入列表并返回，否则返回空列表
        if not root.left and not root.right:
            if root.val == sum:
                lists.append([root.val])
            return lists

        post = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        if post:
            for list in post:
                lists.append([root.val] + list)

        return lists