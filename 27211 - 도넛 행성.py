from collections import deque

def bfs(a, b):
  q = deque()
  q.append([a, b])
  visited[a][b] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + move[i][0]
      ny = y + move[i][1]
      nx = (nx + N) % N
      ny = (ny + M) % M
      if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and planet[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append([nx, ny])

N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1, 0]]
answer = 0

for i in range(N):
  for j in range(M):
    if planet[i][j] == 0 and not visited[i][j]:
      bfs(i, j)
      answer += 1

print(answer)