from collections import deque

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
  a,b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

def bfs(start):
  cnt = 0
  q = deque([start])

  while q:
    cur = q.popleft()
    visited[cur] = True

    for i in arr[cur]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        cnt += 1
  
  print(cnt)
