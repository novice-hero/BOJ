n,m = map(int, input().split())
names = {}
answer = []
for _ in range(n+m):
  name = input()
  if name in names:
    names[name] += 1
  else:
    names[name] = 1

for n in names:
  if names[n] > 1:
    answer.append(n)

answer.sort()
print(len(answer))
for a in answer:
  print(a)