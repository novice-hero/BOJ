def solution(s, n, m):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return

  for i in range(s, n+1):
    answer.append(i)
    solution(i, n, m)
    answer.pop()

n, m = map(int, input().split())
answer = []

solution(1, n, m)