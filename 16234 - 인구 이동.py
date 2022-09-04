from collections import deque

n,l,r = map(int, input().split())
country = []
dx, dy = [1,-1,0,0], [0,0,-1,1]
answer = 0
for _ in range(n):
  country.append(list(map(int, input().split())))

def bfs(a, b, country, visited):
  global check
  q = deque()
  temp = []
  q.append([a,b])
  temp.append([a,b])
  visited[a][b] = True
  
  people = country[a][b]
  count = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
        diff = abs(country[x][y] - country[nx][ny])
        if l<=diff<=r:
          visited[nx][ny] = True
          q.append([nx,ny])
          temp.append([nx,ny])
          people += country[nx][ny]
          count += 1
  
  combine = people//count
  if count>1:
    check = True
    for x,y in temp:
      country[x][y] = combine

while True:
  check = False
  visited = [[False]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        bfs(i,j,country,visited)
  
  if check:
    answer += 1
  else:
    break

print(answer)
