n = int(input())
answer = []
for i in range(n):
    temp = i
    for t in list(str(temp)):
        temp += int(t)
    if temp == n:
        answer.append(i)

if answer:
    print(min(answer))
else:
    print(0)
