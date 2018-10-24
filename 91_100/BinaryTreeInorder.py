# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        order = []
        current = root
        stack = []
        while current:
            # 遍历左子树
            if current.left:
                stack.append(current)
                current = current.left
            # 遍历右子树
            elif current.right:
                order.append(current.val)
                current = current.right
            else:
                order.append(current.val)
                # pop栈顶元素直到元素有右孩子
                while stack and not stack[-1].right:
                    order.append(stack[-1].val)
                    stack.pop()
                if stack:
                    order.append(stack[-1].val)
                    current = stack[-1].right
                    stack.pop()
                else:
                    current = None

        return order


Solution().inorderTraversal(TreeNode(1))