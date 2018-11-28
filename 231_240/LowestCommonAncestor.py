# 235. Lowest Common Ancestor BST
# 236. Lowest Common Ancestor BT


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        if minVal <= root.val <= maxVal:
            return root
        elif root.val > maxVal:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < minVal:
            return self.lowestCommonAncestor(root.right, p, q)


    def lowestCommonAncestorBT(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        # 当root非空时，分别对其左右子树进行搜索，若left，right均非空，则root就是LCA。
        left = self.lowestCommonAncestorBT(root.left, p, q)
        right = self.lowestCommonAncestorBT(root.right, p, q)
        if left and right:
            return root
        # 当左右子树有一个为空时，LCA则在另一颗子树。
        if not left:
            return right
        if not right:
            return left


intervals = [[2,4], [0,2], [3,6], [4,7]]
intervals.sort()
print(intervals)