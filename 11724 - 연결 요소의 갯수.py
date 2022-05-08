from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = 1
  while q:
    cur = q.popleft()
    for i in graph[cur]:
        if visited[i] == 0:
          visited[i] = 1
          q.append(i)

for i in range(1, n+1):
    if visited[i] == 0:
      bfs(i)
      cnt += 1
  
print(cnt)