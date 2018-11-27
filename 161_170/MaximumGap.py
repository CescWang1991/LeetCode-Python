# 164. Maximum Gap
# 利用桶排序

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        gap = self.bucketSort(nums)
        return gap

    def bucketSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
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
            bucket[index].append(nums[i])

        maxGap = 0
        last = None
        for i in range(bucketCount):
            if bucket[i]:
                bucket[i] = sorted(bucket[i])
                for j in range(len(bucket[i])):
                    print(i, j, bucket[i])
                    if j == 0:
                        if last:
                            maxGap = max(maxGap, bucket[i][j] - last)
                    if len(bucket[i]) > 1:
                        maxGap = max(maxGap, bucket[i][j] - bucket[i][j-1])
                        if j == len(bucket[i]) - 1:
                              last = bucket[i][j]
                    else:
                        last = bucket[i][j]
        return maxGap