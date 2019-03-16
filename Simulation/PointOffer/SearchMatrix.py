# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 相似问题：74. Search a 2D Matrix

# 不同处：leetcode 74中每行的第一个整数大于前一行的最后一个整数。

# 思路：首先选取数组中右上角的数字。如果该数字等于要查找的数字，查找过程结束；如果该数字大于要查找的数字，剔除这个数字所
# 在的列；如果该数字小于要查找的数字，剔除这个数字所在的行。


class Solution:
    def find(self, target, array):
        row = 0
        col = len(array[0]) - 1
        while 0 <= row < len(array) and 0 <= col < len(array[0]):
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
                continue
            else:
                row += 1
                continue
        return False
