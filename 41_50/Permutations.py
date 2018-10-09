class Solution(object):
    def permute(self, nums):
        multi = []
        for num in nums:
            rest = nums.copy()
            rest.remove(num)
            if len(rest) == 0:
                multi.append([num])
            else:
                rest_list = Solution().permute(rest)
                for list in rest_list:
                    multi.append([num] + list)

        return multi


print(Solution().permute([1, 2, 3]))
