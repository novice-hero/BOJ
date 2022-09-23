def dfs(depth):
  if depth == 6:
    print(*answer)
    return
  
  if len(answer) == 0:
    for i in s:
      answer.append(i)
      dfs(depth+1)
      answer.pop()
    return

  for i in s:
    if i > answer[len(answer) - 1]:
      answer.append(i)
      dfs(depth+1)
      answer.pop()

while True:
  s = list(map(int, input().split()))
  k = s.pop(0)
  if k==0:
    break
  answer = []

  dfs(0)
  print()