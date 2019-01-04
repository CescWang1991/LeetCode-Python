# 284. Peeking Iterator

# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = -1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)


    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.index += 1
        return self.nums[self.index]

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.flag = False       # 特殊标识符，当第一次调用peek时，将它置为True，表示指针指向下一个节点，当调用next的时候，
                                # 我们知道可以不调用next，而直接返回值。当它为False的时候，next函数照常操作。
        self.curr = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        self.curr = self.next()
        self.flag = True        # 表明指针以指向下一个节点，调用next的时候可以不需要移动指针
        return self.curr

    def next(self):
        """
        :rtype: int
        """
        if not self.flag:
            self.curr = self.iter.next()
        self.flag = False
        return self.curr

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.flag:
            return True
        else:
            return self.iter.hasNext()