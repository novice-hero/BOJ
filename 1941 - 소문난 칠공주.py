from collections import deque

def bfs(arr):
  move = [[0,1],[0,-1],[-1,0],[1,0]]
  visited = [[1]*5 for _ in range(5)]

  for a in arr:
    visited[a[0]][a[1]] = 0

  q = deque()
  q.append(arr[0])
  visited[arr[0][0]][arr[0][1]] = 1
  check = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + move[i][0]
      ny = y + move[i][1]
      if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
        visited[nx][ny] = 1
        check += 1
        q.append([nx, ny])
  
  if check == 7:
    return True
  else:
    return False

def dfs(depth, start, yeon):
  global answer
  
  if yeon >= 4:
    return

  if depth == 7:
    if bfs(arr):
      answer += 1
    return
  
  for i in range(start, 25):
    r = i // 5
    c = i % 5
    arr.append([r, c])
    dfs(depth+1, i+1, yeon+(room[r][c] == 'Y'))
    arr.pop()

room = [list(input()) for _ in range(5)]
arr = []
answer = 0

dfs(0, 0, 0)
print(answer)