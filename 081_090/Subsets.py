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
            if i >= 1 and nums[i] in nums[:i]:
                continue

            post = self.subsets(nums[i+1:])
            for set in post:
                res.append([nums[i]] + set)

        return res


nums = [4, 4, 4, 1, 4]
print(Solution().subsets(nums))