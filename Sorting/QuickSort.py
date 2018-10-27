class Solution:
    def quickSort(self, list):
        if not list or len(list) == 1:
            return list

        pivot = list[0]
        i, j = 1, 1
        while j < len(list):
            if list[j] < pivot:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
                i += 1
            j += 1

        left = list[1: i]
        right = list[i:]

        return self.quickSort(left) + [list[0]] + self.quickSort(right)