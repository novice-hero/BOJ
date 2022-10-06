n,m,k = map(int, input().split())
fireball = []
for _ in range(m):
  r,c,m,s,d = list(map(int, input().split()))
  fireball.append([r-1,c-1,m,s,d])
board = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
  while fireball:
    r,c,m,s,d = fireball.pop(0)
    nr = (r + s * dx[d]) % n
    nc = (c + s * dy[d]) % n
    board[nr][nc].append([m,s,d])

  for i in range(n):
    for j in range(n):
      if len(board[i][j]) > 1:
        sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(board[i][j])
        while board[i][j]:
          _m, _s, _d = board[i][j].pop(0)
          sum_m += _m
          sum_s += _s
          if _d%2:
            odd += 1
          else:
            even += 1
          
        if even == cnt or odd == cnt:
          td = [0,2,4,6]
        else:
          td = [1,3,5,7]
        
        if sum_m//5:
          for d in td:
            fireball.append([i,j,sum_m//5,sum_s//cnt,d])
        
      if len(board[i][j]) == 1:
        fireball.append([i,j]+board[i][j].pop())

print(sum([f[2] for f in fireball]))