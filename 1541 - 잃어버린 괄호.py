words = input().split('-')
answer = 0

for i in words[0].split('+'):
    answer += int(i)
for i in words[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)

