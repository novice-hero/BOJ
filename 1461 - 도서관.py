n, m = map(int, input().split())
loc = list(map(int, input().split()))
plus = [x for x in loc if x > 0]
minus = [x for x in loc if x < 0]
plus.sort(reverse=True)
minus.sort()

max_value = 0
for i in loc:
    if abs(i) > abs(max_value):
        max_value = i

temp = []
for i in range(0, len(plus), m):
    if plus[i] != max_value:
        temp.append(plus[i])
for i in range(0, len(minus), m):
    if minus[i] != max_value:
        temp.append(minus[i])

answer = [abs(x*2) for x in temp]
print(sum(answer)+abs(max_value))

