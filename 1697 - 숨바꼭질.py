from collections import deque
MAX = 100000
n,m = map(int, input().split())
visit = [0]*(MAX+1)

def bfs(n):
  q = deque([n])

  while q:
    cur = q.popleft()
    if cur == m:
      print(visit[cur])
      break

    for i in (cur+1, cur-1, cur*2):
      if i>=0 and i<=MAX and not visit[i]:
        visit[i] = visit[cur] + 1
        q.append(i)

bfs(n)
