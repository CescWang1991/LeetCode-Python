# 099. Recover Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        order = []
        self.dfs(root, order)   # 用递归的方法获取中序遍历，这里的order存放的是树节点，而不是值
        start = 0
        end = len(order) - 1
        while start < end:
            if order[start].val < order[start + 1].val:
                start += 1
            elif order[end].val > order[end - 1].val:
                end -= 1
            else:
                # 找到错误的两个节点，交换其val
                order[start].val, order[end].val = order[end].val, order[start].val
                break

    def dfs(self, node, order):
        if not node:
            return []
        self.dfs(node.left, order)
        order.append(node)
        self.dfs(node.right, order)