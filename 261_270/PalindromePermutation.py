# 266. Palindrome Permutation

# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

# Hint:
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
        count = 0
        for k, v in dict.items():
            if v % 2 == 1:
                count += 1
            if count == 2:      # 奇数个数超过1
                return False

        return True

# 267. Palindrome Permutation II

# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no
# palindromic permutation could be form.

# For example:
# Given s = "aabb", return ["abba", "baab"].
# Given s = "abc", return [].

# Hint:
# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

class Solution2:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: list[str]
        """
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
        mid = ""
        count = 0
        half = ""
        for k, v in dict.items():
            if v % 2 == 1:
                mid = k
                count += 1
                v -= 1      # 对于奇数项，将其个数减一，再当偶数项处理
            if v % 2 == 0:
                dict[k] //= 2
                half += k * dict[k]
            if count == 2:
                return []
        # 对字符串half进行全排列，参见# 047. Permutations II
        self.res = []
        self.permuteUnique(half, "")
        for i in range(len(self.res)):
            self.res[i] = self.res[i] + mid + "".join(list(reversed(self.res[i])))
        return self.res
    # 使用dfs的方法
    def permuteUnique(self, s, ans):
        """
        :type s: str
        :type ans: str
        """
        if not s:
            self.res.append(ans)
            return
        for i in range(len(s)):
            if s[i] not in s[:i]:
                self.permuteUnique(s[:i]+s[i+1:], ans + s[i])
        return