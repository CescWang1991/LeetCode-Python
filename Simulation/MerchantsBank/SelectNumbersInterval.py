# 挑选代表
# 我们有很多区域，每个区域都是从a到b的闭区间，现在我们要从每个区间中挑选至少2个数，那么最少挑选多少个？

# 输入描述：
# 第一行是N（N<10000）,表示有N个区间，之间可以重复
# 然后每一行是ai,bi，持续N行，表示现在区间。均小于100000

# 输出描述：
# 输出一个数，代表最少选取数量。

# 解题思路：
# 贪心，按右端点排序(左端点一样可以)，如果每个区间至少一个点，那么这个点一定是在右端点，这样子可以让后续的区间更容
# 易覆盖到这个点，从而减少选点的数量；同理，如果每个区间至少两个点，那个这个两个点一定也在右端点和右端点前一个点，原因是一样的。

# 答案正确:恭喜！您提交的程序通过了所有的测试用例

def minNumbers(intervals):
    intervals.sort(key=lambda x:x[1], reverse=False)
    nums = []
    for i in range(len(intervals)):
        if not nums or intervals[i][0] > nums[-1]:
            nums.append(intervals[i][1]-1)
            nums.append(intervals[i][1])
        elif intervals[i][0] == nums[-1]:
            nums.append(intervals[i][1])

    return len(nums)

while True:
    try:
        n = int(input())
        intervals = []
        for i in range(n):
            line = input().split(" ")
            a = int(line[0])
            b = int(line[1])
            intervals.append([a, b])
        print(minNumbers(intervals))
    except:
        break