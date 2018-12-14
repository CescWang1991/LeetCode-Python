# 169. Majority Element
# 229. Majority Element II

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if not dict.get(num):
                dict[num] = 1
            else:
                dict[num] += 1
            if dict[num] > len(nums) // 2:
                return num


class Solution2:
    # 运用多数投票算法，详见：https://blog.csdn.net/kimixuchen/article/details/52787307
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        major1, count1 = 0, 0
        major2, count2 = 0, 0
        for num in nums:
            if num == major1:      # 如果数组扫描到的数和当前majority2相等。
                count1 += 1
                continue
            if num == major2:      # 如果数组扫描到的数和当前majority2相等。
                count2 += 1
                continue
            if count1 == 0:        # 针对count1 = 0时，major1为当前值。
                major1 = num
                count1 = 1
                continue
            if count2 == 0:        # 针对count2 = 0时，major2为当前值。
                major2 = num
                count2 = 1
                continue
            count1 -= 1            # 当前num不是1，2时，将1，2的count消去1
            count2 -= 1

        count1, count2 = 0, 0
        # 再次遍历数组判断count1和count2是不是超过三分之一。
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
        res = []
        if count1 > len(nums) // 3:
            res.append(major1)
        if count2 > len(nums) // 3:
            res.append(major2)

        return res


print(Solution2().majorityElement([1,1,1,2,2,3,3,3]))