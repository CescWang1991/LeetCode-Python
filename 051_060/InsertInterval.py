# 057. Insert Intervals

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # 参见#056. Merge Intervals，将newInterval按顺序插入到interval中，然后用合并的方法
    # 注意除了与newInterval有重合的interval，其余的interval不用比较可直接插入merged
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals
        # 将新区间加入到指定位置(按start的顺序)
        for i in range(len(intervals)):
            if intervals[i].start > newInterval.start:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals) - 1: # 注意newInterval成为最后一个的情况
                intervals.append(newInterval)
                break

        merged = []
        for i in range(len(intervals)):
            # 跳过所有end小于start的点和start大于end的点
            if intervals[i].end < newInterval.start or newInterval.end < intervals[i].start:
                merged.append(intervals[i])
                continue
            # 否则，便存在overlap，将interval合并
            if not merged or merged[-1].end < intervals[i].start:   # 当前的interval是整个重合的interval的开头
                merged.append(intervals[i])
            else:
                merged[-1].end = max(merged[-1].end, intervals[i].end)

        return merged