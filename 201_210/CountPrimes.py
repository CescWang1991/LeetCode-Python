# 204. Count Primes
# 建立一个hash table，从2开始遍历至n，如果curr不在hash table中，count++，并且将curr所有小于n的倍数加入到hash table中。

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        curr = 2
        count = 0
        dict = [False] * n
        while curr < n:
            if not dict[curr]:
                count += 1
                i = 2
                while curr * i < n:
                    dict[curr*i] = True
                    i += 1
            curr += 1

        return count