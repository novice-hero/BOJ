from collections import deque

answer = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
box = []
m,n = map(int, input().split())
for _ in range(n):
  temp = list(map(int, input().split()))
  box.append(temp)
q = deque()
for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      q.append((i,j))

def bfs():
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
          q.append((nx,ny))
          box[nx][ny] = box[x][y] + 1

bfs()

for i in box:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(i))

print(answer-1)