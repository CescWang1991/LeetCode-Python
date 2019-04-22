# 077. Combinations

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        lists = []
        if n < k:
            return lists

        for s in reversed(range(k, n+1)):   # 从后往前遍历，这里s是最后一位所有可能的数(s >= k)
            if k == 1:
                lists.append([s])
            else:
                for l in self.combine(s-1, k-1):    # l是s之前的数的列表，注意这里的所有数组都是递增的
                    l += [s]
                    lists.append(l)

        return lists