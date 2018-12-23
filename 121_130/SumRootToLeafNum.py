# 129. Sum Root to Leaf Numbers

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        nums = self.getNums(root)
        sum = 0
        for num in nums:
            sum += int("".join(num))

        return sum

    def getNums(self, root):
        if not root:
            return []
        # if root is a leaf node，从叶节点返回保存节点值的数组
        if not root.left and not root.right:
            return [[str(root.val)]]
        nums = []
        # 父节点将节点值加入到子节点返回数组的头部，合并后返回
        left = self.getNums(root.left)
        if left:
            for post in left:
                nums.append([str(root.val)] + post)
        right = self.getNums(root.right)
        if right:
            for post in right:
                nums.append([str(root.val)] + post)
        return nums

class Solution2:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, sum):       # 传递一个sum参数，代表父节点所产生的和
        if not root:
            return 0
        sum = sum * 10 + root.val   # 父节点的sum比当前节点高一位
        # 加入是叶节点，直接返回sum
        if not root.left and not root.right:
            return sum
        # 返回左右节点的和
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)