# 078. Subsets
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
        # 对于nums的元素，分为取到和没取到两种情况
        term = nums[-1]
        nums.pop(-1)        # 取出数组的最后一个元素
        for list in self.subsets(nums):
            lists.append(list)      # 这里的子集没有取到term
            temp = list + [term]
            lists.append(temp)      # 这里的自己取到了term

        return lists