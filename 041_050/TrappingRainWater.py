# 42. Trapping Rain Water
# Two pointers traversal the array from left and right side. Maintain the max value of both left and right side.
# If the value of current pointer less than maximum, add the subtraction to the area, else, replace the max value.


def trap(height):
    area = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    while left < right:
        if height[left] < height[right]:
            if(height[left] < left_max):
                area += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if (height[right] < right_max):
                area += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1

    return area


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
