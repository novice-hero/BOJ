n, l = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for i in range(n):
    if l >= fruit[i]:
        l += 1

print(l)
