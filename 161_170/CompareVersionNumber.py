# 165. Compare Version Number

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = list(map(lambda x:int(x), version1.split(".")))
        version2 = list(map(lambda x:int(x), version2.split(".")))
        n = min(len(version1), len(version2))
        for i in range(n):
            if int(version1[i]) == int(version2[i]):
                continue
            elif int(version1[i]) > int(version2[i]):
                return 1
            else:
                return -1

        if len(version1) > len(version2) and version1[n:] != [0] * (len(version1) - n):
            print(version1[n:])
            return 1
        elif len(version1) < len(version2) and version2[n:] != [0] * (len(version2) - n):
            return -1
        else:
            return 0