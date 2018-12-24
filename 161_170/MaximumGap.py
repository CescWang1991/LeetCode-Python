# 164. Maximum Gap

class Solution(object):
    # 利用桶排序
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        gap = 0
        nums = self.bucketSort(nums)
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i-1])

        return gap


    def bucketSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 找到nums中的最大值和最小值
        maxVal = nums[0]
        minVal = nums[0]
        for i in range(1,len(nums)):
            maxVal = max(maxVal, nums[i])
            minVal = min(minVal, nums[i])
        bucketLength = (maxVal - minVal) // (len(nums) - 1) + 1
        bucketCount = (maxVal - minVal) // bucketLength + 1

        bucket = [[] for i in range(bucketCount)]
        for i in range(len(nums)):
            index = (nums[i] - minVal) // bucketLength
            if not bucket[index] or nums[i] > bucket[index][-1]:
                bucket[index].append(nums[i])
            else:
                for j in range(len(bucket[index])):
                    if nums[i] <= bucket[index][j]:
                        bucket[index].insert(j, nums[i])
                        break
        res = []
        for i in range(bucketCount):
            res += bucket[i]

        return res

print(Solution().maximumGap([1,1,2,4,5,6,7]))