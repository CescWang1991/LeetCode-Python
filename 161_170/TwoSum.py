# 167. Two Sum II - Input array is sorted
# 我们首先判断首尾两项的和是不是target，如果比target小，那么我们左边+1位置的数（比左边位置的数大）再和右相相加，继续判断。
# 如果比target大，那么我们右边-1位置的数（比右边位置的数小）再和左相相加，继续判断。
# 我们通过这样不断放缩的过程，就可以在O(n)的时间复杂度内找到对应的坐标位置。


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []