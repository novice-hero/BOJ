def dfs(depth):
  if depth == len(word):
    print(''.join(result))
    return
  
  for v in visited:
    if visited[v]:
      visited[v] -= 1
      result.append(v)
      dfs(depth+1)
      visited[v] += 1 
      result.pop()

n = int(input())
for _ in range(n):
  word = sorted(list(input()))
  result = []
  visited = {}

  for w in word:
    if w in visited:
      visited[w] += 1
    else:
      visited[w] = 1

  dfs(0)
