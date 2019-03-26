# 数组中的逆序对

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的
# 总数P。

class Solution:
    def inversePairs(self, data):
        if not data:
            return 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        count = 0
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])

        return count

print(Solution().inversePairs([7, 5, 6, 4]))