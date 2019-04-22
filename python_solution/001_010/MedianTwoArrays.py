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
            return self.findKth(nums1, nums2, 0, 0, length//2+1)

    # 寻找第k小的元素：采用二分法，要寻找第k个元素，先舍弃掉前k个元素中k//2个元素，从nums1或者nums2中去除，我们比较nums中
    # 与nums2中第k//2位元素，从较小的数组中去掉k//2个元素，在从剩余的数组中寻找第k-k//2个元素。
    def findKth(self, nums1, nums2, s1, s2, k):
        """
        :param nums1: 数组1
        :param nums2: 数组2
        :param s1: 数组1的开始值
        :param s2: 数组2的开始值
        :param k:
        :return: 两个数组合并第k小的值
        """
        m = len(nums1)
        n = len(nums2)
        # 若nums1的起始值比m大，则返回nums2中第k个元素，同理可得第二个判别式
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

class Solution2:
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
            return (self.findKth(nums1, nums2, length // 2) + self.findKth(nums1, nums2, length // 2 + 1)) / 2.0
        else:
            return self.findKth(nums1, nums2, length // 2 + 1)

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        m = len(nums1)
        n = len(nums2)
        if k == 1:
            return min(nums1[0], nums2[0])

        mid = k // 2
        # 如果mid大于m，则将k1设为无穷大，因为第mid个值一定在nums2，同理可得。。。
        k1 = float('Inf') if mid > m else nums1[mid - 1]
        k2 = float('Inf') if mid > n else nums2[mid - 1]
        if k1 > k2:
            return self.findKth(nums1, nums2[mid:], k - mid)
        else:
            return self.findKth(nums1[mid:], nums2, k - mid)