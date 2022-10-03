def check(x,y):
  for i in range(5):
    nx = x + dx[i]
    ny = y + dy[i]
    if visited[nx][ny]:
      return False
  return True

def dfs(cnt):
  global answer, total

  if cnt == 3:
    answer = min(answer, total)
    return

  for i in range(1,n-1):
    for j in range(1,n-1):
      if check(i,j):
        for k in range(5):
          ni = i + dx[k]
          nj = j + dy[k]
          visited[ni][nj] = True
          total += board[ni][nj]
        dfs(cnt+1)
        for k in range(5):
          ni = i + dx[k]
          nj = j + dy[k]
          visited[ni][nj] = False
          total -= board[ni][nj]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
answer, total = 1e9, 0

dfs(0)
print(answer)