# 90. Subsets II
# 注意：循环之前要对nums排序

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if not nums:
            return res

        nums.sort()

        for i in range(len(nums)):
            if i >= 1 and nums[i] in nums[:i]:      # 加入当前元素在之前遍历过的元素中再次出现，直接跳过
                continue

            post = self.subsets(nums[i+1:])         # 其余步骤参见 #078。 Subsets
            for set in post:
                res.append([nums[i]] + set)

        return res