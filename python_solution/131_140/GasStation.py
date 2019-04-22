# 134. Gas Station

class Solution:
    # 将cost设为净用量，即cost[i] = gas[i] - cost[i]，然后vol设为到i站时累计的净用量；
    # 我们遍历vol，找到vol的最小值及index，如果vol[n-1]>=0，则表示存在，我们返回index+1；
    # 可以理解为在0站借给它(-minVol)的汽油，它在index处将汽油用光，若在后面的行程中，它的汽油不会用光，则结果为index+1。
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        vol = [0] * n
        vol[0] = cost[0]
        minVol = [gas[0] - cost[0], 0]

        for i in range(1,n):
            cost[i] = gas[i] - cost[i]
            vol[i] = vol[i-1] + cost[i]
            if vol[i] < minVol[0]:
                minVol = [vol[i], i]

        if vol[n-1] >= 0:
            return (minVol[1]+1)%n
        else:
            return -1