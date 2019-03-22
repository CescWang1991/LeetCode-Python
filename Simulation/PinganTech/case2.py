class Solution:
    def minExchange(self, matrix):
        s = self.covert2str(matrix)
        queue = [(s, 0)]
        visited = set()
        visited.add(s)

        while queue:
            p, i = queue[0]
            if p == "123450":
                return i
            index = p.index("0")
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = index // 3 + d[0]
                y = index % 3 + d[1]
                if x < 0 or x >= 2 or y < 0 or y >= 3:
                    continue
                p = list(p)
                p[index], p[x*3 + y] = p[x*3 + y], p[index]
                str = "".join(p)
                if str not in visited:
                    queue.append((str, i+1))
                    visited.add(str)
                p[index], p[x * 3 + y] = p[x * 3 + y], p[index]
            del queue[0]

        return -1

    def covert2str(self, matrix):
        res = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += str(matrix[i][j])

        return res

while True:
    try:
        line = list(input().split("],["))
        a = list(line[0])
        b = list(line[1])
        matrix = [[int(a[2]), int(a[4]), int(a[6])], [int(b[0]), int(b[2]), int(b[4])]]
        print(Solution().minExchange(matrix))
    except:
        break