n, k = map(int, input().split())
money = []
cnt = 0
for _ in range(n):
    money.append(int(input()))
money.sort(reverse=True)

for i in money:
    if k % i != k and k != 0:
        cnt += k // i
        k = k % i

print(cnt)

