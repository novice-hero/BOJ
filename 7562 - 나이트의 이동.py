from collections import deque
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,2,1,-1,-2]

def bfs(a, b):
  q = deque()
  q.append([a,b])

  while q:
    x, y = q.popleft()

    if x == goalX and y == goalY:
          return chessMap[x][y] - 1

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<l and 0<=ny<l and chessMap[nx][ny] == 0:
        chessMap[nx][ny] = chessMap[x][y] + 1   
        q.append([nx, ny])

t = int(input())
for _ in range(t):
  l = int(input())
  curX, curY = map(int, input().split())
  goalX, goalY = map(int, input().split())
  chessMap = [[0]*l for _ in range(l)]
  chessMap[curX][curY] = 1

  print(bfs(curX, curY))