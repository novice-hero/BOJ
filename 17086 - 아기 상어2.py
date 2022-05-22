from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
q = deque()

def bfs():
  answer = 0
  while q:
    x,y = q.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
        q.append((nx,ny))
        arr[nx][ny] = arr[x][y] + 1
        answer = max(answer, arr[x][y])
  return answer

for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      q.append((i,j))

print(bfs())
