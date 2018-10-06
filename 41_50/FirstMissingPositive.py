# Given an unsorted integer array, find the first missing positive integer.
# Your algorithm should run in O(n) time and uses constant space.

# count sort：
# build an array with length of max number that record the counter of each positive number. return i + 1 if arr[i] = 0


def first_missing_positive(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num

    counter = [0] * max
    for num in nums:
        if(num > 0):
            counter[num - 1] += 1

    first = len(counter) + 1
    for i in range(len(counter) - 1):
        if counter[i] == 0:
            first = i + 1
            break

    return first


nums = [1, 2, -1, 4]
print(first_missing_positive(nums))
