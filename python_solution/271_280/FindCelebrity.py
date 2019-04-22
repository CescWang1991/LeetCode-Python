# 277. Find the Celebrity

# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The
# definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is
# to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the
# celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int
# findCelebrity(n), your function should minimize the number of calls to knows.
#
# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a
# celebrity in the party. If there is no celebrity, return -1.

class Solution:
    # 双层嵌套循环，为了节省访问次数，我们设定一个数组isCelebrity来标记，如果不是celebrity，我们标记为False，这样循环时
    # 会跳过一些元素
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        isCelebrity = [True] * n
        for i in range(n):
            if isCelebrity[i]:
                for j in range(n):
                    if self.know(i, j) and i != j:     # i认识j，则i不可能是celebrity，跳出循环
                        isCelebrity[i] = False
                        break
                    elif not self.know(i, j) and i != j:    # i不认识j，则继续，同时j不可能是celebrity，下次循环会跳过
                        isCelebrity[j] = False
                    if j == n:
                        return i
        return -1

    # 系统辅助函数，这里随便写的
    def know(self, a, b):
        return True if (a+b) % 2 == 0 else False