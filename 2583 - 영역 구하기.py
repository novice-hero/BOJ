from collections import deque

M,N,K = map(int, input().split())
area = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
for _ in range(K):
  x1,y1,x2,y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      area[i][j] = 1

def bfs(a,b):
  dx, dy = [1,-1,0,0], [0,0,1,-1]
  q = deque()
  q.append([a, b])
  visited[a][b] = True
  cnt = 1
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<M and 0<=ny<N and area[nx][ny] == 0 and not visited[nx][ny]:
        q.append([nx,ny])
        visited[nx][ny] = True
        cnt += 1
  return cnt

answer = []
for i in range(M):
  for j in range(N):
    if area[i][j] == 0 and not visited[i][j]:
      answer.append(bfs(i,j))

print(len(answer))
print(*sorted(answer))