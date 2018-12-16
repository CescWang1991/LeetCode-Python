class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        sums = [0] * max(m, n)
        carry = 0
        for i in reversed(range(-min(m, n), 0)):
            sum = carry + int(a[i]) + int(b[i])
            if sum == 3:
                carry = 1
                sums[i] = 1
            elif sum == 2:
                carry = 1
                sums[i] = 0
            elif sum == 1:
                carry = 0
                sums[i] = 1
            else:
                carry = 0
                sums[i] = 0

        for j in reversed(range(-max(m, n), -min(m, n))):
            if m > n:
                sum = int(a[j]) + carry
                if sum == 2:
                    sums[j] = 0
                    carry = 1
                elif sum == 1:
                    sums[j] = 1
                    carry = 0
                else:
                    sums[j] = 0
                    carry = 0
            else:
                sum = int(b[j]) + carry
                if sum == 2:
                    sums[j] = 0
                    carry = 1
                elif sum == 1:
                    sums[j] = 1
                    carry = 0
                else:
                    sums[j] = 0
                    carry = 0

        if carry == 1:
            sums.insert(0, 1)

        return ''.join(str(n) for n in sums)


a = "11001"
b = "111"
print(Solution().addBinary(a, b))
