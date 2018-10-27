# Definition for a binary tree node.
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
            father = [root]

            level = 1
            while father:
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

                father = current
                nums = list(map(lambda x: x.val, current))
                if nums:
                    lists.append(nums)
                level +=1

        return lists