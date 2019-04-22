# 046. Permutations
# 047. Permutations II

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

            # added code for 47. Permutation II: continue if the number is in the previous array
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

class Solution2:
    def permuteUnique(self, nums):
        """
        :type s: str
        :type ans: str
        """
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, ans):
        if not nums:
            self.res.append(ans)
            return
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                self.dfs(nums[:i]+nums[i+1:], ans + [nums[i]])
        return