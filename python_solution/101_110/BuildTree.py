# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTreePI(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            root = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])
            leftPreorder = preorder[1: pos+1]
            rightPreorder = preorder[pos+1:]
            leftInorder = inorder[0: pos]
            rightInorder = inorder[pos+1:]

            root.left = self.buildTreePI(leftPreorder, leftInorder)
            root.right = self.buildTreePI(rightPreorder, rightInorder)

            return root
        else:
            return TreeNode(None)

    def buildTreeIP(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            root = TreeNode(postorder[-1])
            pos = inorder.index(postorder[-1])
            leftInorder = inorder[0: pos]
            rightInorder = inorder[pos + 1:]
            leftPostorder = postorder[0: pos]
            rightPostorder = postorder[pos:-1]

            root.left = self.buildTreeIP(leftInorder, leftPostorder)
            root.right = self.buildTreeIP(rightInorder, rightPostorder)

            return root
        else:
            return None