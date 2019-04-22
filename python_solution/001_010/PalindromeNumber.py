# 009. Palindrome Number

class Solution:
    # 将后一半数据翻转，与前一半比较
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        mid = (len(x)-1) // 2
        # 偶数长度前一半包含mid，奇数则不包含，因为翻转的后半部分也不包含mid
        left = x[:mid + 1] if len(x) % 2 == 0 else x[:mid]
        right = x[mid+1:]
        right.reverse()

        return left == right