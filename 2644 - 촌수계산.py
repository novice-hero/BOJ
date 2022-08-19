from collections import deque

def bfs(curr_node):
  queue = deque()
  queue.append(curr_node)
  while queue:
    x = queue.popleft()
    for i in graph[x]:
      if visited[i] == -1:
        visited[i] = visited[x] + 1
        queue.append(i)

N = int(input())
a, b = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[a] = 0
bfs(a)
print(visited[b])