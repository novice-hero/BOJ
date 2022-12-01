def dfs():
  if len(arr) > 0:
    answer.add(int(''.join(map(str, arr))))
  for i in range(0, 10):
    if len(arr)==0 or arr[-1] > i:
      arr.append(i)
      dfs()
      arr.pop()

N = int(input())
arr = []
answer = set()
dfs()
answer = list(answer)
answer.sort()

try:
  print(answer[N-1])
except:
  print(-1)
