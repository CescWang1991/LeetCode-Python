# 255. Verify Preorder Sequence in Binary Search Tree

# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?

# 基本思路：右子节点后面的数不能小于根节点
# [10, 5, 3, 1, 12, 9] 不合法，12是10的右子树，12之后不能出现小于10的数字
# [10, 5, 2, 12，13，11] 不合法，12是13是12的右子树，13之后不能出现小于12的数字

class Solution:
    # 对于一个root节点，以及它的right节点，right节点之后的数都不能小于root节点，而root与right之间的节点构成一个左子树的
    # 前序遍历，可递归调用验证。我们在right之后找到的第一个大于right的节点，说明遍历到了right的右子树，此时将root设为right，
    # right设为当前节点，继续验证。
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        root = 0          # root表示当前根节点的index
        right = 0         # right表示当前节点的右子树的根节点
        for i in range(1, len(preorder)):
            if preorder[right] < preorder[i]:       # 找到第一个比right大的数，将其指定为右子节点
                root = right
                right = i
                leftOrder = preorder[root + 1: i]   # 这个数与root之间的为左子树的谦虚遍历，递归验证
                if not self.verifyPreorder(leftOrder):
                    return False
            if root < right and preorder[root] > preorder[i]:        # 右子节点后面出现了小于root的数，root<right处理初始情况
                return False

        return True