def check(start):
  global answer
  quack = 'quack'
  idx = 0
  flag = False
  for i in range(start, len(sound)):
    if sound[i] == quack[idx] and not visited[i]:
      visited[i] = 1
      if sound[i] == 'k':
        if not flag:
          flag = True
          answer += 1
        idx = 0
        continue
      idx += 1
      

sound = input()
visited = [0]*len(sound)
answer = 0

if len(sound)%5 != 0:
  print(-1)
  exit()

for i in range(len(sound)):
  if sound[i] == 'q' and not visited[i]:
    check(i)

if answer == 0 or not all(visited):
  print(-1)
else:
  print(answer)