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
        result = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        stack = []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right

        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        stack = []
        while stack or root:
            if root:
                stack.append(root)
                result.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left

        return result


node1 = TreeNode(3)
node1.left = TreeNode(1)
node2 = node1.left
node2.right = TreeNode(2)
print(Solution().postorderTraversal(node1))