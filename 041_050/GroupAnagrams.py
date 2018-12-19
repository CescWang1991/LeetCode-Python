# 049. Group Anagrams

from collections import defaultdict

# Categorize by Count:
# Two strings are anagrams if and only if their character counts (respective number of occurrences of each character)
# are the same.

def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()
