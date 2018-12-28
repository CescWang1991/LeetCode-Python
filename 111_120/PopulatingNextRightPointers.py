# 116. Populating Next Right Pointers in Each Node

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :return: nothing
        """
        if not root:
            return
        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

class Solution2:
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :return: nothing
        """
        self.queue = []
        self.dfs(root, 1)

    def dfs(self, root, level):
        if not root:
            return
        if not self.queue or len(self.queue) < level:
            self.queue.append(root)
        else:
            self.queue[level-1].next = root
            self.queue[level-1] = root
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        return