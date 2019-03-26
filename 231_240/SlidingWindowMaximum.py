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

class Solution2:
    # 用双向队列保存数字的下标，队首元素为最大值对应的下标。
    # 遍历整个数组，如果此时队列的首元素是i - k的话，表示此时窗口向右移了一步，则移除队首元素。
    # 然后比较队尾元素和将要进来的值，如果小的话就都移除，然后此时我们把队首元素加入结果中即可。
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        res = []
        import collections
        deque = collections.deque()
        for i in range(k):
            while deque and nums[i] >= nums[deque[-1]]:     # 当遍历到的元素大于队尾元素时，去掉队尾元素
                deque.pop()
            deque.append(i)

        for i in range(k, len(nums)):
            res.append(nums[deque[0]])
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            if deque and deque[0] <= i - k:                 # 此时队首元素不在窗口范围内
                deque.pop(0)
            deque.append(i)
        res.append(nums[deque[0]])
        return res

print(Solution2().maxSlidingWindow([3, 1, 2, 4, 5, 2, 4], 3))