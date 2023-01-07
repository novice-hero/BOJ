R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dx, dy = [1,-1,0,0], [0,0,-1,1]
answer = 1

def bfs():
  global answer
  q = set([(0,0,board[0][0])])
  while q:
    y, x, word = q.pop()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0<=ny<R and 0<=nx<C and board[ny][nx] not in word:
        q.add((ny, nx, word+board[ny][nx]))
        answer = max(answer, len(word)+1)

bfs()
print(answer)