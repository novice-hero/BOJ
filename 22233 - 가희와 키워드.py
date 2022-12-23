import sys

N, M = map(int, sys.stdin.readline().split())
memo = {}
for _ in range(N):
  word = sys.stdin.readline().rstrip()
  if word not in memo:
    memo[word] = 1

answer = N
for _ in range(M):
  keyword = list(sys.stdin.readline().rstrip().split(','))
  for k in keyword:
    if k in memo:
      if memo[k] == 1:
        memo[k] -= 1
        answer -= 1
  print(answer)