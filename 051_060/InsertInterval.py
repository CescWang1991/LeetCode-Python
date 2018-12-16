class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval does not overlap with the previous,
            # simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

    def insertInterval(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        merged = []
        added = False
        for i in range(len(intervals) + 1):
            print(i, len(intervals))
            if not added:
                if intervals[i].start < newInterval.start:
                    merged.append(intervals[i])
                else:
                    intervals.append(newInterval)
                    added = True

            if not merged or merged[-1].end < intervals[i].start:
                merged.append(intervals[i])
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals.
                merged[-1].end = max(merged[-1].end, intervals[i].end)

        return merged


intervals = [Interval(1,2), Interval(4,5), Interval(6,8), Interval(10,12)]
new = Interval(3,5)
print(Solution().insertInterval(intervals, new))