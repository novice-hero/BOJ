n = input()
answer = 0
if n[0] == '0':
    for i in range(len(n) - 1):
        if n[i] == '0' and n[i + 1] == '1':
            answer += 1
if n[0] == '1':
    for i in range(len(n) - 1):
        if n[i] == '1' and n[i + 1] == '0':
            answer += 1

print(answer)
