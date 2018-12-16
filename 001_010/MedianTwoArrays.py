# 4. Median of Two Sorted Arrays
# 解答：https://www.cnblogs.com/lupx/p/lupeixin.html
class Solution:
    # 以总长度奇数为例，k=len//2+1，该问题实际上为在num1和num2组成的数组中寻找第k小的元素
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        length = m + n
        if length % 2 == 0:
            return (self.findKth(nums1, nums2, 0, 0, length//2) + self.findKth(nums1, nums2, 0, 0, length//2+1)) / 2.0
        else:
            return self.findKth(nums1, nums2, 0 ,0 ,length//2+1)
    # 寻找第k小的元素：
    def findKth(self, nums1, nums2, s1, s2, k):
        m = len(nums1)
        n = len(nums2)
        if s1 >= m:
            return nums2[s2 + k - 1]
        if s2 >= n:
            return nums1[s1 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])

        mid = k//2 - 1
        k1 = float('Inf') if s1 + mid >= m else nums1[s1 + mid]
        k2 = float('Inf') if s2 + mid >= n else nums2[s2 + mid]
        if k1 > k2:
            return self.findKth(nums1, nums2, s1, s2 + k//2, k - k//2)
        else:
            return self.findKth(nums1, nums2, s1 + k//2, s2, k - k//2)