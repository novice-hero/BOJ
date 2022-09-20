def solution(n, m):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return

  for i in range(1, n+1):
    answer.append(i)
    solution(n, m)
    answer.pop()

n, m = map(int, input().split())
answer = []

solution(n, m)