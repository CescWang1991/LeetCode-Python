# 八进制加法

class Solution:
    def add(self, a, b):
        carry = 0
        res = []
        while a and b:
            sum = a[0] + b[0] + carry
            if sum >= 8:
                carry = 1
            else:
                carry = 0
            res.append(sum % 8)
            del a[0]
            del b[0]
        while a:
            sum = a[0] + carry
            if sum >= 8:
                carry = 1
            else:
                carry = 0
            res.append(sum % 8)
            del a[0]
        while b:
            sum = b[0] + carry
            if sum >= 8:
                carry = 1
            else:
                carry = 0
            res.append(sum % 8)
            del b[0]
        if carry == 1:
            res.append(1)

        return "".join(list(map(str, reversed(res))))

def reverseInt(num):
    res = []
    while num > 0:
        res.append(num % 10)
        num //= 10
    return res

while True:
    try:
        a = reverseInt(int(input()))
        b = reverseInt(int(input()))
        print(Solution().add(a, b))
    except:
        break