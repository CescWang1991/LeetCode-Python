# 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        res = []
        heap = [-float('Inf')] + nums[:k]
        # 使用最大堆，长度为k
        self.heapBuild(heap)
        res.append(heap[1])
        for i in range(k, len(nums)):
            # 每次迭代，将nums[i-k]替换为nums[i]
            heap[heap.index(nums[i-k])] = nums[i]
            if nums[i] >= heap[1]:
                self.heapBuild(heap)
            res.append(heap[1])

        return res

    def heapBuild(self, heap):
        mid = (len(heap) - 1) // 2
        for i in range(mid):
            # 从最后一个父节点开始调整，直到跟节点
            self.heapAdjust(heap, mid - i)

    def heapAdjust(self, heap, i):
        j = 2 * i
        while j < len(heap):
            if j + 1 < len(heap) and heap[j] < heap[j + 1]:
                j = j + 1
            if heap[i] < heap[j]:
                heap[i], heap[j] = heap[j], heap[i]
                # 交换完毕后，继续检验交换后的节点
                i = j
                j = 2 * i
            else:
                break