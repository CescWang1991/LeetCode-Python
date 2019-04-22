# 124. Binary Tree Maximum Path Sum

class TreeNode:
    def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None

class Solution:
    # 定义数组sum，记录每个root点经过它的最大路径总和，最后取数组中的最大值
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = []
        self.getSum(root, sum)
        print(sum)

        return max(sum)
    # getSum方法返回经过root点的最大单边路径和最大值，方法中的sideSum和pathSum不同点在于：
    # sideSum是从root出发向左子树或右子树延伸的路径，pathSum是经过root的且不包含root父节点的最大路径和。
    # pathSum会加入到数组中，而sideSum作为返回值给父节点，因为经过父节点的路径无法同时包含root的左右子树。
    def getSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: List[int]
        :rtype: int
        """

        if not root:
            return 0

        left = self.getSum(root.left, sum)
        right = self.getSum(root.right, sum)
        sideSum = max(root.val, root.val + left, root.val+ right)
        pathSum = max(sideSum, root.val + left + right)
        sum.append(pathSum)

        return sideSum