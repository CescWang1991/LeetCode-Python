# 298. Binary Tree Longest Consecutive Sequence

# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
# 2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 运用dfs，若左节点或者右节点等于根节点+1，我们遍历子节点，并将长度+1，与max比较
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype:
        """
        self.max = 0
        self.dfs(root, 1)
        return self.max

    def dfs(self, root, length):
        self.max = max(self.max, length)
        if not root:
            return
        if root.left:
            if root.left.val == root.val + 1:   # 左节点时连续的，遍历左节点并长度+1
                self.dfs(root.left, length + 1)
            else:                               # 若不是连续的，则遍历左节点，并将重新赋值长度为1
                self.dfs(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right, length + 1)
            else:
                self.dfs(root.right, 1)