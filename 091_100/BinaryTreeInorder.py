# 094. Binary Tree Inorder Traversal


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
        # 中序遍历，先遍历左子树，到叶节点时，将pop栈中的节点并将值加入res中，然后遍历右子树
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
        # 前序遍历，先将当前节点的值加入res中，然后再遍历左子树，到达节点时pop栈顶，再遍历右子树
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
        # 后序遍历，将当前节点的值加入res的队尾，然后先遍历右子树，再遍历左子树
        while stack or root:
            if root:
                stack.append(root)
                result.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left

        return result