# 排队唱歌
# 我们部门要排队唱歌，大家乱哄哄的挤在一起，现在需要按从低到高的顺序拍成一列，但每次只能交换相邻的两位，请问最少要交换多少次

# 输入描述:
# 第一行是N（N<50000）,表示有N个人
# 然后每一行是人的身高Hi（Hi<2000000,不要怀疑，我们以微米计数），持续N行，表示现在排列的队伍

# 输出描述:
# 输出一个数，代表交换次数。


def minSwitch(nums):
    switch = 0
    if not nums or len(nums) == 1:
        return switch
    while len(nums) > 1:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                switch += 1
        del nums[-1]

    return switch

while True:
    try:
        n = int(input())
        heights = []
        for i in range(n):
            heights.append(int(input()))
        print(minSwitch(heights))
    except:
        break