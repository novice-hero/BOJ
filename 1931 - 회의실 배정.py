N = int(input())

n = sorted(n, key=lambda x: (x[1], x[0]))
start = n[0][1]
answer = 1
for i in range(1, N):
    if start <= n[i][0]:
        start = n[i][1]
        answer+=1

print(answer)