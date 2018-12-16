# 250. Count Univalue Subtrees

# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root:
        :rtype: int
        """
        res = [0]
        self.dfs(root, res)
        return res[0]

    # res作为一个list，可以当作全局变量使用
    def dfs(self, root, res):
        """
        :type root: TreeNode
        :type res: list[int]
        :rtype: bool
        """
        if not root:
            return True
        # 叶节点res直接加1，并返回True
        if not root.left and not root.right:
            res[0] += 1
            return True

        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)
        # 如果左右均为Univalue Subtrees(包含空树)
        if left and right:
            # 列举出root不为Univalue Subtrees的情况，并返回False
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            # 否则，root为Univalue Subtrees，res加一并返回True
            res[0] += 1
            return True

        return False