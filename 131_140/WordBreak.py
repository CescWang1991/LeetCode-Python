def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    if not s:
        return False

    length = len(s)

    # dp(n)代表长度为n的单词是否可分，如果可分，则最后长度为i的单词出现在dict中，同时dp(n-i) = True
    dp = [False] * (length + 1)
    dp[0] = True
    for i in range(length):
        for j in reversed(range(i+1)):
            #从长度为i的单词末尾向前寻找出现在dict中的单词
            sub = s[j:i+1]
            if sub in wordDict and dp[j]:
                dp[i+1] = True
                break

    return dp


def wordSplit(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    index = []
    dp = wordBreak(s, wordDict)

    for i in range(len(dp)):
        if dp[i] and i != 0:
            index.append(i)

    if not index:
        return []

    lists = []

    if s in wordDict:
        lists.append([s])

    for i in index:
        if s[:i] in wordDict:
            res = wordSplit(s[i:], wordDict)
            if res:
                for li in res:
                    li.insert(0, s[:i])
                    lists.append(li)

    return lists


s = "aaaaaaa"
dict = ["a", "aa", "aaaa"]
print(wordSplit(s, dict))