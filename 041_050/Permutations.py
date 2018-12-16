# 46. Permutations and 47. Permutations II
# In Permutations II, continue if the number is in the previous array

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

    def permuteUnique(self, nums):
        multi = []
        for i in range(len(nums)):
            rest = nums.copy()
            del rest[i]

            # added code for 47. Permutation II
            if i != 0 and nums[i] in nums[:i]:
                continue
            # ---------------------------------

            if len(rest) == 0:
                multi.append([nums[i]])
            else:
                rest_list = Solution().permute(rest)
                for list in rest_list:
                    multi.append([nums[i]] + list)

        return multi


print(Solution().permute([1, 1, 2]))
