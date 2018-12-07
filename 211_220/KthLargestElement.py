# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap, nums = nums[:k], nums[k:]
        heap.insert(0, 0)
        # 建立最小堆
        self.heapBuild(heap)

        for num in nums:
            if num > heap[1]:
                heap[1] = num
                self.heapAdjust(heap, 1)
        return heap[1]

    def heapBuild(self, heap):
        mid = (len(heap)-1) // 2
        for i in range(mid):
            # 从最后一个父节点开始调整，直到跟节点
            self.heapAdjust(heap, mid - i)

    def heapAdjust(self, heap, i):
        j = 2 * i
        while j < len(heap):
            if j + 1 < len(heap) and heap[j] > heap[j+1]:
                j = j + 1
            if heap[i] > heap[j]:
                heap[i], heap[j] = heap[j], heap[i]
                # 交换完毕后，继续检验交换后的节点
                i = j
                j = 2 * i
            else:
                break