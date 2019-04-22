# 一个圆被分成M个扇形，一共有N种颜色，相邻扇形不同色，一共有几种涂法？
# 类似于Leetcode 276. Paint Fence

class Solution:
    # 动态规划做法，same[i]表示涂到第i格时，第i格颜色与第0格颜色相同的涂法，diff[i]表示涂到第i格时，第i格颜色与第0格颜色不相同的涂法
    # 状态转移方程，same[i+1] = diff[i]，diff[i+1] = diff[i] * (n-2) + same[i] * (n-1)
    # 最后返回diff[m]即可，我们可以将空间压缩到常数。
    def paintCircle(self, m, n):
        same, diff = 0, n * (n-1)   # 这里初始化表示第1格
        for i in range(2, m):
            temp = same
            same = diff
            diff = diff * (n-2) + temp * (n-1)  # 这里diff需要乘以n-2因为新加的颜色与[0]和[i]均不同

        return diff