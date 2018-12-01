# 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) <= 10:
            return res

        dict = {}
        for i in range(len(s) - 9):
            substr = s[i: i+10]
            if not dict.get(substr):
                dict[substr] = 1
            else:
                if substr not in res:
                    res.append(substr)

        return res

print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAA"))