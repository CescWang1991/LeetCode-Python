# 287. Find the Duplicate Number

class Solution:
    # 快慢指针，由于数字的范围在1-n，而数组的下标范围在0-n，我们可以将nums[i]看成下一个节点的位置
    # 这样这个问题可看作是寻找循环链表的入口节点，可参考#142. Linked List Cycle II
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:    # 两个指针相遇时
                fast = 0
                while True:
                    if slow == fast:
                        return slow
                    slow = nums[slow]
                    fast = nums[fast]

class Solution2:
    # 二分查找，我们在1-n区间范围内查找，首先求出中点mid，然后遍历整个数组，统计所有小于等于mid的数的个数(mid代表下标)，
    # 代表区间[lo, hi]的中点值，如果个数小于等于mid，则说明重复值在[mid+1, n]之间，反之，重复值应在[1, mid-1]之间。
    # 注：此题我们用下标值来表示实际的数，而不是用nums[i]来表示。
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        lo = 0
        hi = n-1
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return hi
    # 以[1,3,4,2,2]为例，<=1的数为1，[lo = mid + 1]，<=2的数为3，[hi = mid]，我们不断缩小区间，直到lo<hi不满足