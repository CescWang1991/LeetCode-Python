# 006. ZigZag Conversion

class Solution:
    # 对于numRows为n的N型，第(n-1)*k列为n个元素，(n-1)*k+1 ... + (n-2)列为1个元素
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        length = numRows * 2 - 2    # 以length长度为单位，分割string
        k = len(s) // length + 1    # 将s分为k个部分，最后一个部分可能不满length
        for i in range(numRows):
            if i == 0 or i == numRows - 1:              # 第一行，shift为0，最后一行，shift为numRows-1，都是i，将其合并
                for j in range(k):
                    if i + length * j < len(s):         # 注意溢出情况
                        res.append(s[i + length * j])
            else:                                       # 其他行，第一个shift为i，第二个shift为length-i
                for j in range(k):
                    if i + length * j < len(s):
                        res.append(s[i + length * j])
                    if length - i + length * j < len(s):
                        res.append(s[length-i+length*j])

        return "".join(res)