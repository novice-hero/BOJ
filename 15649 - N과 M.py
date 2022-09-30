def solution(n, m):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
  
  for i in range(1, n+1):
    if not visited[i]:
      visited[i] = True
      answer.append(i)
      solution(n, m)
      visited[i] = False
      answer.pop()
  
n, m = map(int, input().split())
answer = []
visited = [False]*(n+1)

solution(n, m)