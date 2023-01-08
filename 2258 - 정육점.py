N, M = map(int, input().split())
catalog = [list(map(int, input().split())) for _ in range(N)]
catalog.sort(key=lambda x:(x[1], -x[0]))
answer = []
weight, same = 0, 0

for i in range(N):
  weight += catalog[i][0]
  if i>0 and catalog[i-1][1] == catalog[i][1]:
    same += catalog[i][1]
  else:
    same = 0
  
  if weight >= M:
    answer.append(catalog[i][1]+same)


if len(answer) == 0:
  print(-1)
else:
  print(min(answer))