# 87. Scramble String
# 建立hash table记录两个str中字母的数目，通过比较两个hash table返回是否相等
# 从i=1开始遍历，将s1分为左右子树，s2则可以有i和n-i两种分法，递归比较是s1和s2的子树

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        dict_1 = self.buidDict(s1)
        dict_2 = self.buidDict(s2)
        for k, v in dict_1.items():
            if k not in dict_2.keys() or v != dict_2[k]:
                return False

        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                    or (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                return True

        return False


    def buidDict(self, str):
        dict = {}
        for s in str:
            if s not in dict.keys():
                dict[s] = 1
            else:
                dict[s] += 1

        return dict


s1 = "great"
s2 = "rgeat"
print(Solution().isScramble(s1, s2))