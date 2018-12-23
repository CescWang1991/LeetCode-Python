# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        n = len(s)
        i, j = 0, n-1
        isValid = True
        while i <= j:
            while not s[i].isalpha() and not s[i].isdigit():
                i += 1
                if i not in range(n):
                    break
            while not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                if j not in range(n):
                    break
            if i in range(n) and j in range(n):
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return isValid