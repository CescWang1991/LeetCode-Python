# 038. Count and Say

class Solution:
    # 递归调用，将当前的ans作为helper的输入
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.helper("1", 1, n)

    def helper(self, s, depth, n):
        if depth == n:
            return s
        if len(s) == 1:
            return self.helper("1" + s, 2, n)
        ans = ""
        i, j = 0, 1
        count = 1
        # 双指针，统计对于字符s[i]，有多少个连续元素相同(包括s[i])，将str(count) + s[i]加到ans中
        while j < len(s):
            if s[i] == s[j]:
                j += 1
                count += 1
            else:
                ans += str(count) + s[i]
                i = j
                j += 1
                count = 1
            # 此时遍历到字符串最后，将最后结果加入
            if j == len(s):
                ans += str(count) + s[i]

        return self.helper(ans, depth+1, n)