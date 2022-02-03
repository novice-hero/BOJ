n = int(input())
town = []
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    town.append([x, a])
    people += a
town.sort(key=lambda x: x[0])
half = people / 2

cnt = 0
for t in town:
    cnt += t[1]
    if cnt >= half:
        print(t[0])
        break
