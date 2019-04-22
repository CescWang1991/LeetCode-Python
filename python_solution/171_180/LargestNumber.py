# 179. Largest Number

class Solution:
    # 将nums排序，排序的依据为两个数不同顺序组合的大小
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])

        res = []
        while nums:
            for i in range(len(nums) - 1):
                if not self.larger(str(nums[i]), str(nums[i+1])):
                    nums[i], nums[i+1] = nums[i+1],nums[i]
            res.insert(0, str(nums[-1]))
            nums = nums[:-1]
        if res == ["0"] * len(res):
            res = ["0"]

        return "".join(res)
    # 3 > 30："330" > "303"
    def larger(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        str1 = s1 + s2
        str2 = s2 + s1
        return str1 > str2