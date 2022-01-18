n = int(input())
plus, minus = [], []
answer = 0
for _ in range(n):
    num = int(input())
    if num == 1:
        answer += 1
    elif num > 0:
        plus.append(num)
    else:
        minus.append(num)
plus.sort()
minus.sort(reverse=True)

while len(plus) != 0:
    if len(plus) == 1:
        answer += plus.pop()
    else:
        answer += plus.pop() * plus.pop()

while len(minus) != 0:
    if len(minus) == 1:
        answer += minus.pop()
    else:
        answer += minus.pop() * minus.pop()

print(answer)