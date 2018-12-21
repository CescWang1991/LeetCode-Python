# 088. Merge Sorted Array

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:     # 将nums2[j]插入到i的位置
                nums1.insert(i, nums2[j])
                del nums1[-1]
                i += 1
                j += 1
            else:
                i += 1
        nums1[(m+j):] = nums2[j:]       # 处理nums2的最后几位(均大于nums1的最后一位)