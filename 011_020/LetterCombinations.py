# 017. Letter Combinations of a Phone Number

class Solution:
    # 回溯算法，头数字对应的组合与后面数字返回的结果做笛卡儿积。
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        if not digits:
            return result

        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for char in dict[digits[0]]:
            if len(digits) != 1:
                res = self.letterCombinations(digits[1:])
            else:
                res = [""]

            for str in res:
                result.append(char + str)

        return result