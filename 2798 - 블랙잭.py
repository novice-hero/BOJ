from itertools import combinations

answer = []
n, m = map(int, input().split())
card = list(map(int, input().split()))

temp = list(combinations(card, 3))
temp_sum = [sum(x) for x in temp]

max_sum = 0;
for s in temp_sum:
    if max_sum < s <= m:
        max_sum = s

print(max_sum)
