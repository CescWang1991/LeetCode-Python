# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: Tree
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        dist = abs(root.val - target)
        if target < root.val:
            left = self.closestValue(root.left, target)
            if left and dist < abs(left - target):
                return root.val
            else:               # 不存在左子树或者差值小于左子树返回的差值
                return left
        if target > root.val:
            right = self.closestValue(root.right, target)
            if right and dist < abs(right - target):
                return root.val
            else:               # 不存在右子树或者差值小于右子树返回的差值
                return right

# 272. Closest Binary Search Tree Value II

# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Note:

# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#
# Hint:
#
# 1. Consider implement these two helper functions:
# 　　i. getPredecessor(N), which returns the next smaller node to N.
# 　　ii. getSuccessor(N), which returns the next larger node to N.
# 2. Try to assume that each node has a parent pointer, it makes the problem much easier.
# 3. Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
# 4. You would need two stacks to track the path in finding predecessor and successor node separately.

class Solution2:
    # 利用两个stack，分别保存大于和小于target的节点
    def __init__(self):
        self.ans = []

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: list[int]
        """
        self.pre = []   # 用于存放小于target的最近元素
        self.suc = []   # 用于存放大于target的最近元素
        # 构造一条到离target最近叶节点的路径，pre保存小于target的栈，suc保存大于target的栈。
        while root:
            if root.val <= target:
                self.pre.append(root)
            else:
                self.suc.append(root)
            if not root.left or abs(target - root.left.val) >=  abs(target - root.right.val):
                root = root.right
            elif not root.right or abs(target - root.left.val) <  abs(target - root.right.val):
                root = root.left

        while k > 0:
            # 若suc的栈顶元素比pre的更接近target，我们pop suc，并将suc的栈顶元素的后继路径加入suc中
            if not self.pre or abs(target - self.pre[-1].val) >= abs(target - self.suc[-1].val):
                curr = self.suc.pop()
                self.ans.append(curr)
                self.getSuccessor(curr)
            # 若pre的栈顶元素比suc的更接近target,...
            elif not self.suc or abs(target - self.pre[-1].val) < abs(target - self.suc[-1].val):
                curr = self.pre.pop()
                self.ans.append(curr)
                self.getPredecessor(curr)
            k -= 1
        return self.ans

    def getPredecessor(self, root):
        if not root.left:
            return None
        node = root.left
        while node.right:
            self.pre.append(node)
            node = node.right

    def getSuccessor(self, root):
        if not root.right:
            return None
        node = root.right
        while node.left:
            self.suc.append(node)
            node = node.left

class Solution3:
    # 利用中序遍历进行判断，先将root加入ans，然后中序遍历
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: list[int]
        """
        self.order = []
        # 对order做二分法搜索，找到最近值，然后双指针遍历order

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.order.append(root)
        self.dfs(root.right)