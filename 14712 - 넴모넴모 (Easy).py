n,m = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
answer = 0

def dfs(depth):
  global answer

  if depth == n*m:
    answer += 1
    return
  
  y, x = depth//m+1, depth%m+1

  dfs(depth+1)

  if board[y-1][x]==0 or board[y][x-1]==0 or board[y-1][x-1]==0:
    board[y][x] = 1
    dfs(depth+1)
    board[y][x] = 0

dfs(0)
print(answer)
