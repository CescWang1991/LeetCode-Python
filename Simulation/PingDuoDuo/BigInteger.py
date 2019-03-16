# 大整数相乘

# 有两个用字符串表示的非常大的大整数,算出他们的乘积，也是用字符串表示。不能用系统自带的大整数类型。

# 输入描述:
# 空格分隔的两个字符串，代表输入的两个大整数

# 输出描述:
# 输入的乘积，用字符串表示

# 输入类型为一行字符串，以空格分界，我们用list和split将它转换为列表形式

import sys

# 解法一：
# 参考：https://blog.csdn.net/qq_28203045/article/details/82713070

class Solution1:
    def list2str(self, li):
        while li[0] == 0:
            del li[0]
        res = ''
        for i in li:
            res += str(i)
        return res


    def multi(self, stra, strb):
        aa = list(stra)
        bb = list(strb)
        lena = len(stra)
        lenb = len(strb)
        result = [0 for i in range(lena + lenb)]
        for i in range(lena):
            for j in range(lenb):
                result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
        for i in range(len(result) - 1):
            while result[i] >= 10:
                result[i + 1] += result[i] // 10
                result[i] = result[i] % 10
        return self.list2str(result[::-1])

# 解法二：分治法
class Solution2:
    def calcMulti(self, num1, num2):
        """
        :type num1: list[str]
        :type num2: list[str]
        :rtype: list[str]
        """
        if len(num1) <= 1 or len(num2) <= 1:
            return list(str(int("".join(num1)) * int("".join(num2))))
        a, b = num1[:len(num1)//2], num1[len(num1)//2:]
        c, d = num2[:len(num2)//2], num2[len(num2)//2:]
        list1 = self.calcMulti(a, c) + ['0'] * (len(num1)//2 + len(num2)//2)
        length = len(list1)
        list2 = self.calcMulti(a, d) + ['0'] * (len(num1)//2)
        list2 = [0] * (length - len(list2)) + list2
        list3 = self.calcMulti(b, c) + ['0'] * (len(num2)//2)
        list3 = [0] * (length - len(list3)) + list3
        list4 = self.calcMulti(b, d)
        list4 = [0] * (length - len(list4)) + list4

        res = [0] * length
        carry = 0
        for i in reversed(range(length)):
            sum = int(list1[i]) + int(list2[i]) + int(list3[i]) + int(list4[i]) + carry
            res[i] = str(sum % 10)
            carry = sum // 10
        return res


if __name__ == '__main__':
    while True:
        try:
            line = list(sys.stdin.readline().strip().split(' '))
            if not line:
                break
            num1 = line[0]
            num2 = line[1]
            print("".join(Solution2().calcMulti(list(num1), list(num2))))
        except:
            break