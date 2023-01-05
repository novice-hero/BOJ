from collections import deque

def bfs(a, b):
  visited = [[0]*W for _ in range(H)]
  q = deque()
  q.append([a,b])
  visited[a][b] = 1
  distance = 0

  while q:
    y, x = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= W or ny < 0 or ny >= H:
        continue 
      if tresure_map[ny][nx] == 'L' and not visited[ny][nx]:
        visited[ny][nx] = visited[y][x] + 1
        distance = max(distance, visited[ny][nx])
        q.append([ny, nx])
  
  return distance - 1

dx, dy = [1,-1,0,0], [0,0,-1,1]
H, W = map(int, input().split())
tresure_map = [list(input()) for _ in range(H)]
answer = set()

for i in range(H):
  for j in range(W):
    if tresure_map[i][j] == 'L':
      answer.add(bfs(i,j))

print(max(list(answer)))
