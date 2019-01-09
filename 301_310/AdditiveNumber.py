# 306. Additive Number

class Solution:
    # 运用回溯算法，对num循环，循环i取前i个数作为第一个数，循环j取i+1到j的数作为第二个数，判断剩余后j+1个数前面的位数是否
    # 与两数相加相等，然后递归调用后i+1个数。
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) <= 2:
            return False
        n = len(num)
        for i in range(n // 2):             # 这里对循环剪枝，因为是做加法，所以前两个数位数不能大于第三个数
            if i != 0 and num[0] == "0":    # 这里要注意含0的情况，0可以单独做一个数，但不能作为两位以上的数的开头
                break
            for j in range(i+1, min((n-i-1)//2+i+1, n-i-1)):    # 与i循环同理，对循环剪枝，我们也可以在循环体内加if语句
                                                                # 判断第三个数的位数是否小于前两个数，然后做break
                if j != i+1 and num[i+1] == "0":
                    break
                sum = str(int(num[:i+1]) + int(num[i+1:j+1]))
                if sum == num[j+1:][:len(sum)]:
                    if len(sum) == len(num[j+1:]):
                        return True
                    if self.isAdditiveNumber(num[i+1:]):
                        return True
        return False