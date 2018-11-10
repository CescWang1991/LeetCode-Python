class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        if not digits:
            return result

        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for digit in digits:
            for char in dict[digit]:
                if len(digits) != 1:
                    res = self.letterCombinations(digits[1:])
                else:
                    res = [""]

                for str in res:
                    result.append(char + str)

            return result



print(Solution().letterCombinations("23"))