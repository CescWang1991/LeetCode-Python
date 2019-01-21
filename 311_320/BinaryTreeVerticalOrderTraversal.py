# 314. Binary Tree Vertical Order Traversal

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Examples:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

# Given binary tree [3,9,20,4,5,2,7],
#     _3_
#    /   \
#   9    20
#  / \   / \
# 4   5 2   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,5,2],
#   [20],
#   [7]
# ]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 采用BFS，将遍历到的节点加入queue，并且加入它的列数，root的列设为0，它的left列减一，right列加一，然后用一个dict记录
    # 每一列所对应的列表，遍历时将节点值加入所对应列的列表即可。
    def verticalOrder(self, root):
        """
        :type root:
        :rtype: list[list[int]]
        """
        TreeMap = {}
        queue = [(root, 0)]
        TreeMap[0] = [root.val]
        while queue:
            curr = queue[0][0]
            mark = queue[0][1]
            del queue[0]
            if curr.left:
                queue.append((curr.left, mark-1))
                if not TreeMap.get(mark-1):
                    TreeMap[mark - 1] = [curr.left.val]
                else:
                    TreeMap[mark - 1].append(curr.left.val)
            if curr.right:
                queue.append((curr.right, mark+1))
                if not TreeMap.get(mark+1):
                    TreeMap[mark + 1] = [curr.right.val]
                else:
                    TreeMap[mark + 1].append(curr.right.val)
        TreeMap = sorted(TreeMap.items(), key=lambda x:x[0])
        res = []
        for map in TreeMap:
            res.append(map[1])
        return res