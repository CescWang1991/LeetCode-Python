# 041. First Missing Positive

def firstMissingPositive(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    # 建立数组，记录每一个正数出现的次数
    counter = [0] * max
    for num in nums:
        if(num > 0):
            counter[num - 1] += 1
    # 遍历counter，找到第一个0出现的地方
    first = len(counter) + 1
    for i in range(len(counter) - 1):
        if counter[i] == 0:
            first = i + 1
            break

    return first
