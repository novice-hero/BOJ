N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
maze = [[0]*(M+1) for _ in range(N+1)]
for n in range(N):
  for m in range(M):
    maze[n+1][m+1] = arr[n][m]

for i in range(1, N+1):
  for j in range(1, M+1):
    maze[i][j] = max(maze[i-1][j]+maze[i][j], maze[i][j-1]+maze[i][j], maze[i-1][j-1]+maze[i][j])

print(max(maze[-1]))