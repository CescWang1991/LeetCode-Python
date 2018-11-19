# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dict = {}
        longest = 0
        # 建立字典，key为数组中的每个数字
        for num in nums:
            dict[num] = 0
        # 遍历数组中的每个数字，以当前数字为起点，向左/向右查询，如果存在于字典中，则将长度+1，继续查询。
        # 将遍历过的数字(包括当前数字)从字典中删除，这样遍历数组时不会出现重复遍历。
        for num in nums:
            if num not in dict.keys():
                continue

            del dict[num]
            length = 1
            left = num - 1
            while left in dict.keys():
                length += 1
                del dict[left]
                left -= 1
            right = num + 1
            while right in dict.keys():
                length += 1
                del dict[right]
                right += 1

            longest = max(longest, length)

        return longest


nums = [1, 2, 0, 1]
print(Solution().longestConsecutive(nums))