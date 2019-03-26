# 二叉搜索树与双向链表

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.lastNode = None  # 这里的lastNode表示已经转换过的链表的最后一个节点

    def convertBST(self, root):
        if root:
            return root
        self.convertNode(root)
        head = self.lastNode
        while head and head.left:
            head = head.left

        return head

    def convertNode(self, root):
        if not root:
            return root
        curr = root
        # 中序遍历，先访问左子树
        if curr.left:
            self.convertNode(root.left)
        # 此时lastNode为左子树所形成的链表的最后一个节点
        curr.left = self.lastNode
        if self.lastNode:
            self.lastNode.right = curr
        # 此时curr为链表的最后一个节点
        self.lastNode = curr

        if curr.right:
            self.convertNode(curr.right)