def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

while True:
    try:
        line = list(map(int, input().split(",")))
        x, y, z = line[0], line[1], line[2]
        print(z == 0 or (x + y >= z and z % gcd(x, y) == 0))
    except:
        break