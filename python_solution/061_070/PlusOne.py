# 066. Plus One

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits

        carry = 1
        for i in reversed(range(len(digits))):
            carry = 1 if (digits[i] + carry) >= 10 else 0
            digits[i] = (digits[i] + carry) % 10

        if carry == 1:
            digits.insert(0, 1)

        return digits