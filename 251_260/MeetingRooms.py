# 252. Meeting Rooms

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
# if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def canAttendMeetings(self, v):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        v.sort(key=lambda x: x.start)
        # any()函数用于判断给定的可迭代参数iterable是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
        return not any(v[i].start < v[i-1].end for i in range(1, len(v)))

# 253. Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
# minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

class Solution2:
    # 对起始时间进行排序，使用最小堆来记录当前会议的结束时间，当心会议的起始时间大于最小堆中的最早结束时间，说明新会议与
    # 堆中的最早结束会议不重叠。
    def minMeetingRooms(self, v):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        v.sort(key=lambda x: x[0])  # 将数组按起始时间排序
        minHeap = []    # 建立最小堆表示当前会议室的结束时间，按时间从小到大排序(这里忽略最小堆的实现)
        rooms = 0
        for i in range(len(v)):
            if not minHeap or v[i][0] < minHeap[0]:     # 若会议时间小于结束会议的最小时间，则需要一个新房间
                rooms += 1
            elif v[i][0] >= minHeap[0]:                 # 不需要新房间，将最小的结束时间代替
                del minHeap[0]
            minHeap.append(v[i][1])                     # 加入当前的会议结束时间
            minHeap.sort()                              # 这里可以用最小堆的调整算法