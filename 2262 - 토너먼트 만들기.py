n = int(input())
lank = list(map(int, input().split()))
answer = 0

for i in range(len(lank) - 1):
    target = max(lank)
    idx = lank.index(target)
    if idx == 0:
        answer += target - lank[1]
    elif idx == len(lank) - 1:
        answer += target - lank[-2]
    else:
        answer = min(answer + target - lank[idx - 1], answer + target - lank[idx + 1])

    del lank[idx]

print(answer)
