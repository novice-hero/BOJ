from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
n,m = map(int, input().split())
war = [list(map(str, input())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
white, blue = 0, 0

def bfs(a,b):
  q = deque()
  q.append([a, b])
  visited[a][b] = True
  color = war[a][b]
  cnt = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and war[nx][ny] == color:
        q.append([nx, ny])
        visited[nx][ny] = True
        cnt += 1

  return cnt + 1

for i in range(m):
  for j in range(n):
    if war[i][j] == 'W' and not visited[i][j]:
      white += bfs(i,j)**2
    elif war[i][j] == 'B' and not visited[i][j]:
      blue += bfs(i,j)**2

print(white, blue)