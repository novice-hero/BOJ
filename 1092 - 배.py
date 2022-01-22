# PyPy3로 제출해야함
n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crain.sort(reverse=True)
box.sort(reverse=True)

if crain[0] < box[0]:
    print(-1)
    exit()

answer = 0
while len(box) > 0:
    for i in range(n):
        for j in range(len(box)):
            if crain[i] >= box[j]:
                del box[j]
                break
    answer += 1

print(answer)
