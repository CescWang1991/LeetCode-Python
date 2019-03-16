# 最大乘积

# 题目描述
# 给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)

# 输入描述:
# 无序整数数组A[n]

# 输出描述:
# 满足条件的最大乘积

# 输入情况：第一行为一个整数，第二行为一个整数数组

import sys
while True:
    try:
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        if n == '' or line == '':
            break
        nums = list(map(lambda x: int(x), line.split()))
        ####
        if not nums or len(nums) < 3:
            print(None)
            break
        minOne, minTwo = 0, 0
        maxOne, maxTwo, res = 0, 0, 0
        for num in nums:
            res = max(res, num * maxTwo, num * minTwo)
            if num == 0:
                continue
            elif num > 0:
                minTwo = min(minTwo, num * minOne)
                maxTwo = max(maxTwo, num * maxOne)
            else:
                minTwo = min(minTwo, num * maxOne)
                maxTwo = max(maxTwo, num * minOne)
            minOne = min(num, minOne)
            maxOne = max(num, maxOne)
        ####
        print(res)
    except:
        break