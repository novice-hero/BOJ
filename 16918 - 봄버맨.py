from collections import deque

def checkBomb():
  for i in range(r):
    for j in range(c):
      if board[i][j] == 'O':
        bombs.append([i,j])

def makeBomb():
  for i in range(r):
    for j in range(c):
      if board[i][j] == '.':
        board[i][j] = 'O'

def explosion():
  dx, dy = [1,0,-1,0], [0,-1,0,1]
  while bombs:
    x, y = bombs.popleft()
    board[x][y] = '.'
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<r and 0<=ny<c:
        board[nx][ny] = '.'

r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)] # 1단계

n -= 1 # 2단계
while n:
  bombs = deque()
  checkBomb()
  makeBomb() # 3단계
  n-=1
  if n == 0:
    break
  explosion() # 4단계
  n-=1

for i in range(r):
  print(''.join(board[i]))
