# 146. LRU Cache

import collections

class LRUCache:
    # 引入OrderedDict，实现了对字典对象中元素的排序，使用OrderedDict会根据放入元素的先后顺序进行排序。
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.dict = collections.OrderedDict()
    # get操作时，若key存在，返回value，同时先将key-value删除，再插入，这样key的顺序就来到头部。
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        except:
            return -1

    # The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in
    # LIFO order if last is true or FIFO order if false.
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            del self.dict[key]
            self.dict[key] = value
        except:
            if self.length == self.capacity:
                self.dict.popitem(last=False)
                self.length -= 1
            self.dict[key] = value
            self.length += 1