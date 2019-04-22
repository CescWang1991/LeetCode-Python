# 295. Find Median from Data Stream

# 我们使用大小堆来解决问题:
#       我们用自定义的Heap类型实现一个最小堆，然后将右半边的大的元素放入large中
#       然后我们将左半边小的元素取负加入small中，这样small堆顶的负数就是最大元素

class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = Heap()
        self.small = Heap()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.large.push(num)
        self.small.push(-self.large.top())    # prev的堆顶为最小元素，将其负数加入post中
        self.large.pop()
        if self.large.size() < self.small.size():
              self.large.push(-self.small.top())  # prev的堆顶为最大元素的负数，将其负数加入prev中
              self.small.pop()

    def findMedian(self):
        """
        :rtype: float
        """
        if self.large.size() == self.small.size():
            return float(self.large.top() - self.small.top()) / 2
        else:
            return float(self.large.top())

class Heap:
    # 实现一个最小堆，堆顶为最小元素
    def __init__(self):
        self.heap = [0]

    def push(self, num):
        self.heap.insert(1, num)
        self.adjust(1)

    def top(self):
        return self.heap[1]

    def pop(self):
        del self.heap[1]
        self.adjust(1)

    def size(self):
        return len(self.heap) - 1

    def adjust(self, i):
        j = 2 * i
        while j < len(self.heap):
            if j + 1 < len(self.heap) and self.heap[j] > self.heap[j+1]:
                j = j+1
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
            j = 2 * i