class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start)


class Solution:
    def merge(self, intervals):
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


print(Solution().merge([Interval(0, 3), Interval(0, 4), Interval(1, 2), Interval(4, 5)]))
