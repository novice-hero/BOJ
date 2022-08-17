import sys
input = sys.stdin.readline
R,C,T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
up,down = -1,-1

for i in range(R):
  if room[i][0] == -1:
    up = i
    down = i+1
    break

def spreadDust():
  dx,dy = [1,-1,0,0], [0,0,1,-1]
  tempArr = [[0]*C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if room[i][j] != 0 and room[i][j] != -1:
        temp = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0<=nx<R and 0<=ny<C and room[nx][ny] != -1:
            tempArr[nx][ny] += room[i][j]//5
            temp += room[i][j]//5
        room[i][j] -= temp
  
  for i in range(R):
    for j in range(C):
      room[i][j] += tempArr[i][j]

def airCleaner_Up():
  dx,dy = [0,-1,0,1], [1,0,-1,0] # 우 상 좌 하
  x, y = up, 1
  temp = 0
  d = 0
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if x==up and y==0:
      break
    if nx>=R or nx<0 or ny>=C or ny<0:
      d+=1
      continue
    else:
      room[x][y], temp = temp, room[x][y]
      x, y = nx, ny

def airCleaner_Down():
  dx,dy = [0,1,0,-1], [1,0,-1,0] # 우 하 좌 상
  x, y = down, 1
  temp = 0
  d = 0
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if x==down and y==0:
      break
    if nx>=R or nx<0 or ny>=C or ny<0:
      d+=1
      continue
    else:
      room[x][y], temp = temp, room[x][y]
      x, y = nx, ny

for _ in range(T):
  spreadDust()
  airCleaner_Up()
  airCleaner_Down()

answer = 0
for i in range(R):
  for j in range(C):
    if room[i][j] > 0:
      answer += room[i][j]

print(answer)