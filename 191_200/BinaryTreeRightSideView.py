# 199. Binary Tree Right Side View
# BFS：从根节点出发，从右向左遍历子节点。维持一个队列queue，将遍历过的节点加入队列，然后访问子节点后再删除。
# 维持一个结果数组res，先将根节点及其level加入数组，在遍历节点时，若将要删除的节点层数位res最后一个的层数+1，那我们将它加入res。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        res.append((root.val, 1))
        queue = [(root, 1)]

        while queue:
            curr = queue[0][0]
            level = queue[0][1]
            if curr.right:
                queue.append((curr.right, level+1))
            if curr.left:
                queue.append((curr.left, level+1))
            if level == res[-1][1] + 1:
                res.append((queue[0][0].val, queue[0][1]))
            del queue[0]

        return list(map(lambda x:x[0], res))

class Solution2:
    # 利用dfs，若res的长度小于当前level，我们新添加一层，否则继续遍历，因为我们总是先遍历右子树，所以新添加的一行总是该
    # 层最右边的节点
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root, 1)
        return self.res

    def dfs(self, root, level):
        if not root:
            return
        if not self.res or len(self.res) < level:   # 添加新的一行
            self.res.append(root.val)
        if root.right:                              # 先遍历右子树
            self.dfs(root.right, level+1)
        if root.left:                               # 再遍历左子树
            self.dfs(root.left, level+1)
        return