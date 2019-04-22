# 250. Count Univalue Subtrees

# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root:
        :rtype: int
        """
        bol, res = self.dfs(root)
        return res

    # dfs返回两个参数，第一个表示root含subtree的个数，第二个表示root是否为uni subtree
    def dfs(self, root):
        """
        :type root: TreeNode
        :type res: list[int]
        :rtype: bool
        """
        if not root:
            return True, 0
        # 叶节点res直接加1，并返回True
        if not root.left and not root.right:
            return True, 1

        left, leftVal = self.dfs(root.left)
        right, rightVal = self.dfs(root.right)
        # 如果左右均为Univalue Subtrees(包含空树)
        if left and right:
            # 列出root为Univalue Subtrees的所有情况
            if (not root.left and root.val == root.left.val) or (not root.right and root.val == root.right.val) or \
                    (root.val == root.left.val == root.right.val):
                return True, 1

        return False, leftVal + rightVal