# Merge Sort

def mergeSort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    # 将数组按照middle进行递归拆分
    mid = length // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    # 将其使用对两个有序数组进行排序的方法对其进行排序
    return merge(left, right)


def merge(left, right):
    res = []
    # 同时对两个数组的第一个位置进行比大小，将小的放入一个空数组，然后被放入空数组的那个位置的指针往后移一个
    # 然后继续和另外一个数组的上一个位置进行比较.
    while left and right:
        if left[0] >= right[0]:
            res.append(left[0])
            del left[0]
        else:
            res.append(right[0])
            del right[0]
    # 到最后任何一个数组先出栈完，就将另外i一个数组里的所有元素追加到新数组后面。
    if not left:
        res += right
    if not right:
        res += left

    return res


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(mergeSort(a))