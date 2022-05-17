from collections import deque

n = int(input())
area = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt1, cnt2 = 0, 0

def bfs(a,b):
  q = deque()
  q.append((a,b))
  visited[a][b] = True
  color = area[a][b]

  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and area[nx][ny] == color:
        q.append((nx,ny))
        visited[nx][ny] = True

# 적록색약 아닌 경우
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt1 += 1

visited = [[False]*n for _ in range(n)]

# 적록색약
for i in range(n):
  for j in range(n):
    if area[i][j] == 'R':
      area[i][j] = 'G'
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt2 += 1


print(cnt1, cnt2)
