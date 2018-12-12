# Count Complete Tree Nodes

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 如果右子树的高度等于整棵二叉树的高度-1的话，那么左子树一定是一棵满二叉树，这个时候我们就很容易的计算出总结点数
    # nodes=2**(h)-1 + 1 +右子树节点数（这里的+1表示root节点）。
    # 如果右子树的高度不等于整棵二叉树的高度-1的话，那么左子树不一定是一棵满二叉树，但右子树一定是一棵满二叉树，
    # 这个时候我们就很容易的计算出总结点数nodes=2**(h-1)-1 + 1 +左子树节点数（这里的+1表示root节点）。
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        h = self.height(root)
        nodes = 0
        while root:
            # 右子树的高度为h-1，则左子树一定是满二叉树(高度h-1)，则左子树结点数量为2**(h-1)-1
            if self.height(root.right) == h - 1:
                # 增量包含root结点
                nodes += 2**(h-1)
                # 左子树不需要遍历，直接遍历右子树
                root = root.right
            # 右子树的高度为h-2，则右子树一定是满二叉树(高度h-2)，则右子树结点数量为2**(h-2)-1
            else:
                # 增量包含root结点
                nodes += 2**(h-2)
                # 右子树不需要遍历，直接遍历左子树
                root = root.left
            h -= 1

        return nodes

    def height(self, root):
        if not root:
            return 0
        h = 0
        while root:
            root = root.left
            h += 1
        return h