# 292. Nim Game

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2 or n == 3:
            return True
        if n == 4:
            return False

        return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))
        # return n % 4 != 0 上述做法会导致超时，由此我们可以发现规律，只要是4的倍数个，我们一定会输，所以对4取余即可