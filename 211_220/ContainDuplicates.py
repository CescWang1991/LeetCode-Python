# 217. Contains Duplicates
# 219. Contains Duplicates II
# 220. Contains Duplicates III

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        dict = {}
        for num in nums:
            if not dict.get(num):
                dict[num] = 1
            else:
                return True

        return False


class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        dict = {}
        for i in range(len(nums)):
            if not dict.get(nums[i]):
                dict[nums[i]] = [i]
            else:
                if abs(i - dict[nums[i]][-1]) <= k:
                    return True
                else:
                    dict[nums[i]].append(i)

        return False

class Solution3:
    # 维持一个k长度的窗口，遍历到第i项时，在窗口中寻找是否存在数num，使得nums[i] - t <= num <= nums[i] + t。
    # 正常遍历窗口k，需要时间复杂度为O(nk)，使用基于BST的结构(TreeSet，Python中没有)，可以在logk时间内找出是否存在。
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k == 0 or k >= 10000:
            return False

        s = set()
        s.add(nums[0])
        for i in range(1, len(nums)):
            for elem in s:
                if abs(elem - nums[i]) <= t:
                    return True

            s.add(nums[i])
            if len(s) == k + 1:
                s.remove(nums[i - k])

        return False