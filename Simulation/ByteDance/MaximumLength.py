class Solution:
    def get(self, n, m, L):
        if n > m:
            L = L[:m]
        while m > len(L):
            v = L[0] / 2
            del L[0]
            if v < L[-1]:
                L.append(v)
                L.append(v)
            else:
                for i in range(len(L)):
                    if v >= L[i]:
                        L.insert(i, v)
                        L.insert(i, v)
                        break
        while m == len(L):
            if L[0] / 2 > L[-1]:
                v = L[0] / 2
                del L[0]
                del L[-1]
                if v < L[-1]:
                    L.append(v)
                    L.append(v)
                for i in range(len(L)):
                    if v >= L[i]:
                        L.insert(i, v)
                        L.insert(i, v)
                        break
            else:
                break
        print("{:.2f}".format(L[-1]))

Solution().get(3, 4, [16.0, 8.0, 3.0])