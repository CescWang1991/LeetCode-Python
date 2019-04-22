# 285. Inorder Successor in BST

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# Note: If the given node has no in-order successor in the tree, return null.

class Solution:
    # 利用BST性质，假如p的值小于root，则遍历左子树，否则遍历右子树
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p)
        if p.val > root.val:
            return self.inorderSuccessor(root.right, p)
        # 此时root正好是p，我们则寻找其右子树的最左节点，注意右子树为空的情况
        root = root.right
        while root and root.left:
            root = root.left
        return root