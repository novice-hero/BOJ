from collections import deque
n,m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

def bfs(a,b):
  dx, dy = [1,0,-1,0], [0,1,0,-1]
  q = deque()
  q.append([a,b])
  visited[a][b] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        if iceberg[nx][ny] == 0 and iceberg[x][y] >= 1:
          melting_arr[x][y] += 1
        else:
          q.append([nx, ny])
          visited[nx][ny] = True
  
  return 1

check = False
answer = 0
while True:
  result = []
  visited = [[False]*m for _ in range(n)]
  melting_arr = [[0]*m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if iceberg[i][j] != 0 and visited[i][j] == False:
        result.append(bfs(i,j))

  for i in range(n):
    for j in range(m):
      iceberg[i][j] -= melting_arr[i][j]
      if iceberg[i][j] < 0:
        iceberg[i][j] = 0

  if len(result) == 0:
    break
  if len(result) >= 2:
    check = True
    break
  answer += 1

if check:
  print(answer)
else:
  print(0)