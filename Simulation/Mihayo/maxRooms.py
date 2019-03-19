class Solution:
    def maxValue(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        counts = 0
        for i in range(len(intervals)):
            if not heap or intervals[i][0] < heap[0]:
                counts += 1
            elif intervals[i][0] >= heap[0]:
                del heap[0]
            heap.insert(0, intervals[i][1])
            heap = self.adjust(heap)

        return counts

    def adjust(self, heap):
        heap.insert(0, 0)
        i, j = 1, 2
        while j < len(heap):
            if j + 1 < len(heap) and heap[j] > heap[j+1]:
                j = j + 1
            if heap[i] > heap[j]:
                heap[i], heap[j] = heap[j], heap[i]
                i = j
                j = 2 * i
            else:
                break

        del heap[0]
        return heap