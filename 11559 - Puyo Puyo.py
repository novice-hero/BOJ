from collections import deque

arr = [list(input()) for _ in range(12)]

def down():
  for i in range(6):
    for j in range(10, -1, -1):
      for k in range(11, j, -1):
        if arr[j][i] != "." and arr[k][i] == ".":
          arr[k][i] = arr[j][i]
          arr[j][i] = "."
          break

def bfs(a,b,s):
  dx, dy = [1,0,-1,0], [0,-1,0,1]
  visited = [[False]*6 for _ in range(12)]
  count = 1
  plus = 0

  q, change = deque(), deque()
  q.append([a,b])
  change.append([a,b])
  visited[a][b] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<len(arr) and 0<=ny<len(arr[0]) and not visited[nx][ny]:
        if arr[nx][ny] == s:
          q.append([nx, ny])
          change.append([nx, ny])
          visited[nx][ny] = True
          count += 1
    if count >= 4:
      plus = 1
      for x, y in change:
        arr[x][y] = '.'
  
  return plus

answer = 0
while True:
  temp = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] != '.':
        temp += bfs(i,j,arr[i][j])
  if temp == 0:
    print(answer)
    break
  else:
    answer += 1
  down()