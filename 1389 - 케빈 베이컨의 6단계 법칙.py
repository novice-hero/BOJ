from collections import deque

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

def bfs(x):
  visited = [0] * (n+1)
  q = deque()
  q.append(x)
  visited[x] = 1

  while q:
    node = q.popleft()
    for i in friends[node]:
      if not visited[i]:
        visited[i] = visited[node] + 1
        q.append(i)
  
  return sum(visited)

answer = []
for i in range(1, n+1):
  answer.append(bfs(i))

print(answer.index(min(answer))+1)