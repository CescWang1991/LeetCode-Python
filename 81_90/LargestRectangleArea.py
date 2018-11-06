def largestRectangleArea(nums):
    if not nums:
        return 0

    nums.append(0)
    length = len(nums)
    m = 0
    stack = []
    i = 0
    while i < length:
        if not stack or nums[i] >= nums[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            h = nums[stack[-1]]
            stack.pop()
            if not stack:
                m = max(m, h * i)
            else:
                m = max(m, h * (i - stack[-1] -1))

    return m