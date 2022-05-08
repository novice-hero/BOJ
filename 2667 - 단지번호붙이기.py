from collections import deque

n = int(input())
apart = []
apartCnt = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
  apart.append(list(map(int, input())))

def bfs(a, b):
  q = deque()
  q.append([a,b])
  apart[a][b] = 0
  cnt = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and apart[nx][ny] == 1:
        q.append([nx,ny])
        apart[nx][ny] = 0
        cnt+=1
  
  return cnt

for i in range(n):
  for j in range(n):
    if apart[i][j] == 1:
      apartCnt.append(bfs(i,j))

apartCnt.sort()
print(len(apartCnt))
for i in range(len(apartCnt)):
  print(apartCnt[i])