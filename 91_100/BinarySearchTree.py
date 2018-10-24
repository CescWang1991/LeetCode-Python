# Dynamic Programming
# 拿到n个数字后，从中依次选取一个作为根结点，遍历其左子树和右子树的所有方法的所有笛卡尔积组合，累加，作为该点作为根节点的方法数。

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0] = res[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                res[i] += res[j] * res[i-1-j]

        return res[n]


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        trees = self.getTrees(1, n)

        return trees

    def getTrees(self, s, e):
        if s > e:
            return [None]

        trees = []

        for val in range(s, e + 1):
            left = self.getTrees(s, val - 1)
            right = self.getTrees(val + 1, e)
            for leftTree in left:
                for rightTree in right:
                    root = TreeNode(val)
                    root.left = leftTree
                    root.right = rightTree
                    trees.append(root)

        return trees


print(Solution().generateTrees(3))