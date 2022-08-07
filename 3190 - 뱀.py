from collections import deque
n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
  a,b = list(map(int, input().split()))
  board[a-1][b-1] = 2

l = int(input())
dic = {}
for _ in range(l):
  a,b = input().split()
  dic[int(a)] = b

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(d, v):
  if v=='L':
    d = (d-1)%4
  else:
    d = (d+1)%4
  return d

x,y = 0,0
board[x][y] = 1
direction = 0
time = 0
dq = deque()
dq.append([0,0])

while True:
  time+=1
  x += dx[direction]
  y += dy[direction]

  if x<0 or x>=n or y<0 or y>=n:
    break
  
  if board[x][y] == 2:
    board[x][y] = 1
    dq.append([x,y])
    if time in dic:
      direction = turn(direction, dic[time])

  elif board[x][y] == 0:
    board[x][y] = 1
    dq.append([x,y])
    a, b = dq.popleft()
    board[a][b] = 0
    if time in dic:
      direction = turn(direction, dic[time])
  
  else:
    break

print(time)
