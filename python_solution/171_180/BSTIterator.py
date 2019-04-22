# 173. Binary Search Tree Iterator

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 将中序遍历的功能嵌查在整个程序中
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr = root
        self.iter = []
        if not root:
            self.iter = []
        else:
            # 因为只可能是左节点才是最小值，将所有左子树节点入栈，保证空间复杂度是O(h)
            while self.curr:
                self.iter.append(self.curr)
                self.curr = self.curr.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.iter else False

    def next(self):
        """
        :rtype: int
        """
        self.curr = self.iter.pop()
        # 这一步已经得到最小值
        res = self.curr
        # 但要考虑到右子树的遍历
        self.curr = self.curr.right
        while self.curr:
            self.iter.append(self.curr)
            self.curr = self.curr.left

        return res