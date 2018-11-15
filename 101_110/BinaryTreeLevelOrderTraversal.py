# 102. Binary Tree Level Order Traversal
# 107. Binary Tree Level Order Traversal II

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        order = [[]]
        # 队列记录树节点与它所在的层数
        queue = [(root, 0)]
        while queue:
            curr = queue[0]
            if len(order) < curr[1] + 1:
                order.append([])
            order[curr[1]].append(curr[0].val)

            del queue[0]
            # 如果存在左右子节点，将它们加入队列，对应层数是当前层数+1
            if curr[0].left:
                queue.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                queue.append((curr[0].right, curr[1]+1))

        return order

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        order = [[]]
        # 队列记录树节点与它所在的层数
        queue = [(root, 0)]
        while queue:
            curr = queue[0]
            # 与上一题不同的是，当order的大小小于当前层数+1时，我们将curr插入到order最前面，然后将元素添加在order的第一项
            if len(order) < curr[1] + 1:
                order.insert(0, [])
            order[0].append(curr[0].val)

            del queue[0]
            # 如果存在左右子节点，将它们加入队列，对应层数是当前层数+1
            if curr[0].left:
                queue.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                queue.append((curr[0].right, curr[1]+1))

        return order