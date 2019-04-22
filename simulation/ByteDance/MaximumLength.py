class Solution:
    def get(self, m, L):
        L = list(map(float, sorted(L, reverse=True)))
        lo = 0
        hi = L[0]
        while lo <= hi:
            print(lo, hi)
            mid = (lo + hi) / 2
            if self.enough(mid, m, L):
                lo = mid
            else:
                hi = mid - 0.01
        return "{:.2f}".format(lo)

    def enough(self, length, m, L):
        count = 0
        for i in range(len(L)):
            count += int(L[i] // length)
        return True if count >= m else False
