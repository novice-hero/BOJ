# PyPy3
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num.sort()

answer = 0
for i in range(1, n+1):
    answer += abs(i-num[i-1])

print(answer)
