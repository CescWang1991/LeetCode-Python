class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ""
        if not s or not t or len(s) < len(t):
            return result

        dict_t = self.buildDict(t)
        min = ""
        for i in range(len(s)):
            if s[i] not in dict_t.keys():
                continue
            for j in range(i+1, len(s)+1):
                if j - i < len(t):
                    continue
                else:
                    dict_s = self.buildDict(s[i: j])
                    if self.compDicts(dict_s, dict_t):
                        if not min or len(s[i: j]) < len(min):
                            min = s[i: j]
        return min


    def buildDict(self, s):
        dict = {}
        for c in s:
            if c not in dict.keys():
                dict[c] = 1
            else:
                dict[c] += 1

        return dict

    def compDicts(self, dict_s, dict_t):
        comp = True
        for k, v in dict_t.items():
            if k not in dict_s.keys():
                comp = False
            elif dict_s[k] < dict_t[k]:
                comp = False
        return comp


s = "wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon"
t = "ozgzyywxvtublcl"
print(Solution().minWindow(s, t))
