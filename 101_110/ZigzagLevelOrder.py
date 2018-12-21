# 103. Binary Tree Zigzag Level Order Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lists = []
        if root:
            lists.append([root.val])

            # 列表father用来存放上一层以遍历过的节点
            father = [root]

            level = 1
            while father:
                # 按层遍历，在当前层，按逆序遍历father，在奇数层(从0开始)先记录右子节点，再记录左子节点，偶数层相反
                current = []
                # From left to right
                if level % 2 == 0:
                    for node in reversed(father):
                        if node.left:
                            current.append(node.left)
                        if node.right:
                            current.append(node.right)
                # From right to left
                elif level % 2 == 1:
                    for node in reversed(father):
                        if node.right:
                            current.append(node.right)
                        if node.left:
                            current.append(node.left)
                # 将父节点设为当前层，用于下一层遍历
                father = current
                nums = list(map(lambda x: x.val, current))
                if nums:
                    lists.append(nums)
                level +=1

        return lists

class Solution2:
    # 递归调用方法，采用DFS，level记录当前节点的层数，类似 #102与 #107的方法
    # 如果flag为false，表示正序输出，使用add，否则使用addFirst，反向输出。
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.levelRecur(root, ans, 1, False)
        return ans

    def levelRecur(self, root, ans, level, reverse):
        if not root:
            return
        if len(ans) < level:
            ans.append([root.val])
        else:
            if reverse:
                ans[level-1].insert(0, root.val)
            else:
                ans[level-1].append(root.val)
        self.levelRecur(root.left, ans, level+1, not reverse)
        self.levelRecur(root.right, ans, level + 1, not reverse)