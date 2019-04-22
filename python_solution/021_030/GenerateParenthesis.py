# 022. Generate Parentheses

class Solution:
    # 分治法，在一个有效的括号"（）"中，括号中间有a个有效括号，右边有b个，则a+b+1 = n，然后分别递归调用
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return [""]
        elif n == 1:
            return ["()"]

        list = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    list.append("(" + left + ")" + right)

        return list