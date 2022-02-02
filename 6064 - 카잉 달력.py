t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    nobody = True
    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            nobody = False
            break
        x += m
    if nobody:
        print(-1)
