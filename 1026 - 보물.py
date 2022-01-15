n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

answer = []
for i in range(n):
    answer.append(a[i]*b[i])

print(sum(answer))
