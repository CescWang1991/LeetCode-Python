# n个整数的无序数组，找到每个元素后面比它大的第一个数，要求时间复杂度为O(N)

# 1、栈里面保留是索引，而非元素，其实这是一个很关键的地方，索引的信息要比内容多，因为可以索引本身就可以确定内容。要牢记这一特点
# 2、初始栈，里面为第一个元素
# 3、如果栈不为空，而且当前处理元素比栈顶元素大，则栈顶元素对应的第一个比它大的值，就是该元素
# 4、弹出栈顶元素，继续处理栈里的元素，直至为空或当前处理元素不大于栈顶元素
# 5、将当前元素压入栈
# 6、循环3~5

class Solution:
    def getFirstLargerNum(self, nums):
        stack = []
        stack.append(0)
        i = 1
        res = [None] * len(nums)
        while i < len(nums):
            if stack and nums[i] > nums[stack[-1]]:
                res[stack[-1]] = nums[i]
                stack.pop()
            else:
                stack.append(i)
                i += 1
        print(res)


nums = [2, 1, 3, 6, 7, 5]
Solution().getFirstLargerNum(nums)