n = int(input())
people = list(map(int, input().split()))
people.sort()

temp = []
cnt = 0
while True:
    if cnt == n:
        break
    total = 0
    for i in range(cnt+1):
        total += people[i]
    temp.append(total)
    cnt += 1
answer = sum(temp)

print(answer)

# 더 나은 풀이
# n = int(input())
# people = list(map(int, input().split()))
# num = 0
# people.sort()
# 
# for i in range(n):
#     for j in range(i + 1):
#         num += people[j]
# print(num)