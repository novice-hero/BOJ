n,m = map(int, input().split())
maze = []
for _ in range(n):
  maze.append(list(map(int, input())))
# 동서남북
dx = [1,-1,0,0]
dy = [0,0,-1,1]

q = [[0,0]]

while q:
  x, y = q.pop(0)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < m and maze[nx][ny] == 1:
      q.append([nx,ny])
      maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1])