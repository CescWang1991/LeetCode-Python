from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        dict_t = Counter(t)
        n = len(dict_t)
        contain = False
        if m < n:
            return ""
        for j in range(n, m+1):
            for i in range(m-j+1):
                sub = s[i:i+j]
                dict_s = Counter(sub)
                formed = 0
                for key in dict_t.keys():
                    if dict_s[key] >= dict_t[key]:
                        formed += 1
                if formed == n:
                    contain = True
                    return sub

        if not contain:
            return ""


s = "zfvdiuibotzsqrpgfnbfwudczyruzvuyaselommcfmuxdmgkzhpydsafttzsowrrovccjqhpcdohpurpeiphdrmwkooykfracvemmldqpragmtxqcmxfdmbnapomxfmzdqlpeofvghbubzkdnjirxlgxaujzcxzfqmuudbrllsfmtrpjczaakgzmdlofinkybgugjlrugygzrxiuwkwitvxwilbranrbvmigzbbfcjhthrpfclqxjntrawkajcdgqlmpppxrzemivcpzpfwauruuneuyiyeylrqagnthrgpokhozmmaheudryysjywhjpzmymhhfnxwxemzsyzbcvfwvfoedmoocnccckjjzifzoryhqxkuurspwgubtkqxxuzbeilersdhkdoccbywsrlpxhssriprdqujzhnsaszmvqoxrotjfhafqtxkdpbifvsgfhafccr"
t = "xshxlvswdb"
print(Solution().minWindow(s, t))
