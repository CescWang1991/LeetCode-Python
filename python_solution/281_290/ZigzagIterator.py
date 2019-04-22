# 281. Zigzag Iterator

# Given two 1d vectors, implement an iterator to return their elements alternately.
# For example, given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you,
# replace "Zigzag" with "Cyclic". For example, given the following input:
#
# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].

class ZigzagIterator:
    # 在初始化的时候就两个数组按照之字形的顺序存入另一个一位数组中
    def __init__(self, v1, v2):
        self.iter = []
        length = min(len(v1), len(v2))
        for i in range(length):
            self.iter.append(v1[i])
            self.iter.append(v2[i])
        if len(v1) != length:
            self.iter += v1[length:]
        else:
            self.iter += v2[length:]
        self.index = 0
        self.length = len(v1) + len(v2)

    def next(self):
        self.index += 1
        return self.iter[self.index]

    def hasNext(self):
        return True if self.index < self.length else False