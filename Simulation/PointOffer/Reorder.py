def ReorderOddEven(nums):
    '''
    :type nums: list[int]
    :return: none
    '''
    if not nums:
        return None

    p = 0
    q = 0
    while p < len(nums):
        if nums[p] % 2 == 1:
            nums[p], nums[q] = nums[q], nums[p]
            q += 1
        p += 1

    print(nums)