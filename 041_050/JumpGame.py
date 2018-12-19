# 045. Jump Game II

# We use "last" to keep track of the maximum distance that has been reached by using the minimum steps "ret",
# whereas "curr" is the maximum distance that can be reached by using "ret+1" steps.
# Thus,curr = max(i+A[i]) where 0 <= i <= last.


class Solution(object):
    def jump(self, A):
        ret = 0
        last = 0        # last用来记录用当前步数steps所能到达的最大距离
        curr = 0        # curr是steps+1步能达到的最大距离
        for i in range(len(A)):
            if i > last:    # 当前遍历到的点大于last，步数加一
                last = curr
                ret += 1
            curr = max(curr, i + A[i])
        return ret
