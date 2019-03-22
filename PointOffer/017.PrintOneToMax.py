# 017.打印从1到最大的N位数

# 输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。

class Solution:
    # 利用全排列方法把n位的每一位从0到9排列一遍，就得到所有十进制的数。
    def printNDigits(self, n):
        if n <= 0:
            return
        nums = ["0"] * n
        for i in range(10):
            nums[0] = str(i)
            self.printRecursively(nums, n, 0)

    def printRecursively(self, nums, length, index):
        if index == length - 1:
            self.printNums(nums)
            return
        for i in range(10):
            nums[index+1] = str(i)
            self.printRecursively(nums, length, index+1)

    def printNums(self, nums):
        for i in range(len(nums)):
            if nums[i] != "0":
                print("".join(nums[i:]))
                break