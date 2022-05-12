from collections import deque

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]

def bfs(x, y):
    m[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
      a, b = q.popleft()
      for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:
          m[nx][ny] = 0
          q.append([nx, ny])

while True:
  w, h = map(int, input().split())
  if w==0 and h==0:
    break
  m = []
  answer = 0
  for _ in range(h):
    m.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if m[i][j] == 1:
        bfs(i,j)
        answer += 1
  
  print(answer)
