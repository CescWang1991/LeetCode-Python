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


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))