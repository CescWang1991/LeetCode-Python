# 78. Subsets
# subset(n) = subset(n-1) + subset(n-1).append(n)

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lists = []
        if not nums:
            return [[]]

        while nums:
            term = nums[-1]
            nums.pop(-1)
            for list in self.subsets(nums):
                lists.append(list)
                temp = list + [term]
                lists.append(temp)

        return lists


nums = [1, 2, 3, 4]
print(Solution().subsets(nums))
