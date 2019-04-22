# 042. Trapping Rain Water

def trap(height):
    area = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    # 双指针从两边向中间遍历，维持左右两边的最大值
    while left < right:
        if height[left] < height[right]:    # 右边高，则更新左边值
            if(height[left] < left_max):    # 与max比较，小于增将差值加入到area中
                area += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:                               # 左边高，则更新右边值
            if (height[right] < right_max):
                area += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1

    return area
