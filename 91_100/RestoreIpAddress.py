# 93. Restore Ip Addresses
# Backtracking: 构造辅助函数helper, 返回s所能构造的ip地址的前n位

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        ips = self.helper(s, 4)

        return ips

    def helper(self, s, n):
        ips = []
        if n == 1:
            if len(s) == 1:
                ips.append(s)
            elif len(s) == 2 and int(s[0]) != 0:
                ips.append(s)
                ips.append(".".join(s))
            elif len(s) == 3 and int(s[0]) != 0:
                if int(s) in range(0, 256):
                    ips.append(s)
        elif n in range(2, 5):
            if len(s) > 1:
                for ip in self.helper(s[1:], n-1):
                    if ip.count(".") == n-2:
                        ips.append(s[0]+"."+ip)

            if len(s) > 2 and int(s[0]) != 0:
                for ip in self.helper(s[2:], n-1):
                    if ip.count(".") == n-2:
                        ips.append(s[:2]+"."+ip)

            if len(s) > 3 and int(s[0]) != 0 and int(s[:3]) in range(0, 256):
                for ip in self.helper(s[3:], n-1):
                    if ip.count(".") == n-2:
                        ips.append(s[:3] + "." + ip)

        return ips


print(Solution().restoreIpAddresses("255255255255"))