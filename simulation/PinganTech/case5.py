class Solution:
    def threeSum(self, nums):
        hash = {}
        res = []
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        if 0 in hash and hash[0] >= 3:
            res.append([0, 0, 0])
        neg = list(filter(lambda x: x < 0, hash))
        pos = list(filter(lambda x: x >= 0, hash))
        for i in neg:
            for j in pos:
                diff = 0 - i - j
                if hash.get(diff) != None:
                    if diff in (i, j) and hash[diff] >= 2:
                        res.append([i, j, diff])
                    if diff < i or diff > j:
                        res.append([i, j, diff])
        res.sort(reverse=True)

        return res

while True:
    try:
        line = input().split("[")[1]
        line = line.split("]")[0]
        nums = list(map(int, line.split(",")))
        results = Solution().threeSum(nums)
        for result in results:
            result.sort()
            print(result[0], result[1], result[2])
    except:
        break