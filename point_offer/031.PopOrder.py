# 栈的压入、弹出元素

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如
# 序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV or len(pushV) != len(pushV):
            return False
        stack = []
        i, j = 0, 0
        while i < len(pushV) or j < len(popV):
            if i < len(pushV):
                stack.append(pushV[i])
                if stack[-1] == popV[j]:
                    stack.pop()
                    j += 1
                i += 1
            else:
                if stack[-1] == popV[j]:
                    stack.pop()
                    j += 1
                else:
                    return False

        return True

print(Solution().IsPopOrder([1,2,3,4,5], [4,3,5,1,2]))