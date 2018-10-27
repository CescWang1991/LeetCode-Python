class Solution:
    def findNum(self, list):
        if not list:
            return None

        start = 0
        end = len(list) - 1
        while start < end:
            mid = int((start + end) / 2)
            if list[mid] > list[end]:
                start = mid + 1
            else:
                end = mid

        return list[start]


list = [4, 5, 6, 7, 1, 2, 3]
print(Solution().findNum(list))