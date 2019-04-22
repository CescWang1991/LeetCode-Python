# 056. Merge Intervals

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start)


class Solution:
    def merge(self, intervals):
        # 将intervals按照开始位置排序
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # 如果merged为空或者当前interval没有覆盖(overlap)前一个，将其添加
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            # 否则，我们将当前区间与merged的最后区间合并
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
