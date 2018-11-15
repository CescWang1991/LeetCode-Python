# 103. Binary Tree Zigzag Level Order Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lists = []
        if root:
            lists.append([root.val])

            # 列表father用来存放上一层以遍历过的节点
            father = [root]

            level = 1
            while father:
                # 按层遍历，在当前层，按逆序遍历father，在奇数层(从0开始)先记录右子节点，再记录左子节点，偶数层相反
                current = []
                # From left to right
                if level % 2 == 0:
                    for node in reversed(father):
                        if node.left:
                            current.append(node.left)
                        if node.right:
                            current.append(node.right)
                # From right to left
                elif level % 2 == 1:
                    for node in reversed(father):
                        if node.right:
                            current.append(node.right)
                        if node.left:
                            current.append(node.left)
                # 将父节点设为当前层，用于下一层遍历
                father = current
                nums = list(map(lambda x: x.val, current))
                if nums:
                    lists.append(nums)
                level +=1

        return lists