while True:
    try:
        line = list(map(int, input().split()))
        n, m = line[0], line[1]
        matrix = []
        for i in range(n):
            matrix.append(list(input()))
        print(matrix)
    except:
        break