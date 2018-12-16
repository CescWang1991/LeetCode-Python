# 39. Combination Sum
# 40. Combination Sum II
# 216. Combination Sum III

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        if not candidates:
            return result

        for num in candidates:
            if target == num:
                result.append([num])
            else:
                if target > num:
                    res = self.combinationSum(candidates[candidates.index(num):], target - num)
                    if res:
                        for list in res:
                            result.append([num] + list)

        return result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        if not candidates:
            return result

        candidates.sort()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] in candidates[:i]:
                continue

            if target == candidates[i]:
                result.append([candidates[i]])
            elif target > candidates[i]:
                res = [] if i == len(candidates) - 1 else candidates[i+1:]
                lists = self.combinationSum2(res, target - candidates[i])
                if lists:
                    for list in lists:
                        result.append([candidates[i]] + list)

        return result

    # 定义一个辅助函数help，其中s表示数字1-9循环开始的数字，后面的post数组中元素都要大于s
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.help(k, n, 1)

    def help(self, k, n, s):
        res = []
        if k <= 0 or k > n or k * 9 < n or s > 9:
            return res
        if k == 1 and s <= n <= 9:
            return [[n]]

        for i in range(s, 10):
            post = self.help(k-1, n - i, i+1)
            if post:
                for elem in post:
                    res.append([i] + elem)

        return res