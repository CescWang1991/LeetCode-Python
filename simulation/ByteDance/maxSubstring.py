class Solution:
    def findMaxSubstring(self, s, n, m):
        i, j = 0, 0
        countA, countB = 0, 0
        if s[0] == "a":
            countA += 1
        else:
            countB += 1
        res = 0
        while i <= j and j < n - 1:
            if countA <= m or countB <= m:
                res = max(res, j - i + 1)
                j += 1
                if s[j] == "a":
                    countA += 1
                else:
                    countB += 1
            else:
                i += 1
                if s[i - 1] == "a":
                    countA -= 1
                else:
                    countB -= 1
        return res

if __name__ == "__main__":
    print(Solution().findMaxSubstring("aabaabaa", 8, 1))