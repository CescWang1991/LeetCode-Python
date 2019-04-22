# 二叉搜索树的后序遍历序列

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数
# 字都互不相同。

class Solution:
    def verifyBST(self, nums):
        if not nums:
            return True
        root = nums[-1]
        index = 0
        for i in range(len(nums) - 1):
            if nums[i] > root:
                index = i
                break
        # #如果在右子树中有比根节点小的值，直接返回False
        for i in range(index, len(nums) - 1):
            if nums[i] < root:
                return False

        left = nums[:index]
        right = nums[index: len(nums)-1]

        return self.verifyBST(left) and self.verifyBST(right)