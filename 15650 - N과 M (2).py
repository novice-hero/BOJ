def solution(s, n, m):
  if len(answer) == m:
    print(' '.join(map(str, answer)))

  for i in range(s, n+1):
    if i not in answer:
      answer.append(i)
      solution(i+1, n, m)
      answer.pop()

n, m = map(int, input().split())
answer = []

solution(1, n, m)