# 015. 3Sum
# 016. 3Sum Closest
# 018. 4Sum

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        result = list()
        # num_hash来记录nums中数字的个数
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        # 如果有超过3个0
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])
        # 我们可以通过两个list去存取nums中含有不重复元素的正数和负数。
        neg = list(filter(lambda x: x < 0, nums_hash))
        pos = list(filter(lambda x: x >= 0, nums_hash))
        # 那么在三个数不全为0的情况下，必然有一个正数和一个负数
        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    # 假如dif和i或j重复，并且dif在数组中出现两次以上
                    if dif in (i, j) and nums_hash[dif] >= 2:
                        result.append([i, j, dif])
                    # 对于a,b,c三个数，如果a是正数，b是负数，那么-c一定比b大，或者比a小
                    if dif < i or dif > j:
                        result.append([i, j, dif])

        return result


class Solution2:
    # 将nums排序，遍历数组，指定双指针，遍历当前元素后面的元素，从两边向中间遍历，比较sum和target的距离与维持的最小值。
    # 如果sum小于target，我们希望sum增长，所以l += 1，反之r -= 1。 时间复杂度应该是O(n²)。
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dist = float('Inf')
        res = 0
        for i in range(len(nums)-2):
            # 从两头开始遍历
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if dist > abs(target - sum):
                    dist = abs(target - sum)
                    res = sum
                if target > sum:
                    l += 1
                else:
                    r -= 1
        return res

class Solution3:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_hash = {}
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        print(nums_hash)
        dict = {}
        result = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                diff = target - nums[i] - nums[j]
                # 如果diff在dict中，我们将它的位置数组提取出来
                if dict.get(diff):
                    for pos in dict[diff]:
                        if pos[1] < i:      # 这里可以限定顺序以避免重复，即pos[0] < pos[1] < i < j
                            # 排序并去重
                            ans = sorted([nums[pos[0]], nums[pos[1]], nums[i], nums[j]])
                            if ans not in result:
                                result.append(ans)
                # 将nums[i]与nums[j]的和假如dict，当作key，将i和j组成的数组作为value。
                if not dict.get(sum):
                    dict[sum] = [[i, j]]
                else:
                    dict[sum].append([i, j])
        return result