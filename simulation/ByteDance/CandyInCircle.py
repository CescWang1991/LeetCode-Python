# 类似Leetcode 135. Candy
# 不同处在于这里形成一个环状，所以需要四次循环[1]，或者从ratings的最小值开始遍历

class Solution:
    def minRewards(self, k, ratings):
        if not ratings:
            return 0
        if k == 2:
            return 3 if ratings[0] != ratings[1] else 2
        reward = [1] * k
        if ratings[k-1] < ratings[0]:
            reward[0] = reward[k-1] + 1
        for i in range(1, k):
            if ratings[i-1] < ratings[i]:
                reward[i] = reward[i-1] + 1

        if ratings[k-1] > ratings[0]:
            reward[k-1] = max(reward[k-1], reward[0] + 1)
        for i in reversed(range(1, k)):
            if ratings[i-1] > ratings[i]:
                reward[i-1] = max(reward[i-1], reward[i] + 1)

        if ratings[k-1] < ratings[0]:
            reward[0] = max(reward[0], reward[k-1] + 1)
        for i in range(1, k):
            if ratings[i-1] < ratings[i]:
                reward[i] = max(reward[i], reward[i-1] + 1)

        if ratings[k-1] > ratings[0]:
            reward[k-1] = max(reward[k-1], reward[0] + 1)
        for i in reversed(range(1, k)):
            if ratings[i-1] > ratings[i]:
                reward[i-1] = max(reward[i-1], reward[i] + 1)

        return sum(reward)


L = [1, 2, 3, 3]
print(Solution().minRewards(len(L), L))