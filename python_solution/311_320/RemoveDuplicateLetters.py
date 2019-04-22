# 316. Remove Duplicate Letters

class Solution:
    # 构建字典counts，记录每个字母的个数，构建visited字典，记录字母是否被访问
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        counts = {}
        visited = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            visited[char] = False
        ans = ""
        for char in s:
            counts[char] -= 1
            if visited[char]:       # 如果当前字母被访问了，我们直接跳过
                continue
            if not ans:             # 第一个字母加入ans，并设对应的visited为True
                ans += char
                visited[ans] = True
            else:
                while ans and char < ans[-1] and counts[ans[-1]] > 0:   # 从ans末尾遍历，如果末尾字母排序大于当前字母
                                                                        # 并且剩余的count不为0，我们将末尾从ans删除，并设False
                    visited[ans[-1]] = False
                    ans = ans[:-1]
                ans += char         # 将当前的字母加入ans，并设True
                visited[ans[-1]] = True
        return ans