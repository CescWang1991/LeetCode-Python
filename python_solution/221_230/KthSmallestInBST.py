# 230. Kth Smallest Element in a BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 构造一个辅助函数，运用递归中序遍历方法将BST展开到一个数组中，然后查找数组的第k-1个元素
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = self.flattenBST(root)
        return res[k-1]

    def flattenBST(self, root):
        """
        :type root: TreeNode
        :rtype: list[int]
        """
        if not root:
            return []

        return self.flattenBST(root.left) + [root.val] + self.flattenBST(root.right)

class Solution2:
    # 构造辅助函数计算树的节点个数，如果左size >= k，则说明element在左子树，遍历左子树递归调用(root.left, k)
    # 如果左size == k - 1，则说明root就是我们要的点，否则遍历右子树递归调用(root.right, k - size - 1)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0

        leftSize = self.countTreeNodes(root.left)
        if leftSize > k - 1:
            return self.kthSmallest(root.left, k)
        elif leftSize == k - 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k-leftSize-1)

    def countTreeNodes(self, root):
        if not root:
            return 0

        return self.countTreeNodes(root.left) + 1 + self.countTreeNodes(root.right)