# 315. Count of Smaller Numbers After Self

class SearchTreeNode:
    # 构建二叉搜索树，其中count用来记录小于val的点的个数
    def __init__(self, x):
        self.val = x
        self.count = 0
        self.left = None
        self.right = None

class Solution:
    # 二分查找，数组从后往前遍历，将遍历到的数加入到新的数组，新的数组实现排序，用二分插入法将新元素插入，然后返回它的
    # index-1即为对应的数量
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        counts = [0] * len(nums)
        sorting = [nums[-1]]
        for i in reversed(range(len(counts) - 1)):
            curr = nums[i]
            if curr > sorting[-1]:
                sorting.append(curr)
                counts[i] = len(sorting) - 1
            else:
                lo, hi = 0, len(sorting) - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if sorting[mid] < curr:
                        lo = mid + 1
                    elif sorting[mid] >= curr:
                        hi = mid
                sorting.insert(hi, curr)
                counts[i] = hi
        return counts

class Solution2:
    # 利用bisect维持有序数组
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        sorting = []
        counts = []
        for num in reversed(nums):
            index = bisect.bisect_left(sorting, num)
            sorting.insert(index, num)
            counts.append(index)
        return list(reversed(counts))