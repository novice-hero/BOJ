from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,m,k = map(int, input().split())
arr = [['.']*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
trash = []

for _ in range(k):
  a,b = map(int, input().split())
  arr[a-1][b-1] = '#'

def bfs(a,b):
  q = deque()
  q.append((a,b))
  visited[a][b] = True
  cnt = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == '#':
        q.append((nx,ny))
        visited[nx][ny] = True
        cnt += 1
    
  return cnt

for i in range(n):
  for j in range(m):
    if arr[i][j] == '#' and not visited[i][j]:
      trash.append(bfs(i,j))

print(max(trash))