import sys
input = sys.stdin.readline

def dfs(start, next, cost, visited):
  global min_cost
  if len(visited) == n:
    if city[next][start] != 0:
      min_cost = min(min_cost, cost+city[next][start])
    return
  
  for i in range(n):
    if city[next][i] != 0 and i not in visited and cost < min_cost:
      visited.append(i)
      dfs(start, i, cost+city[next][i], visited)
      visited.pop()

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
min_cost = 1e9

for i in range(n):
  dfs(i,i,0,[i])

print(min_cost)
