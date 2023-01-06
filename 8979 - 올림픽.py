N, K = map(int, input().split())
record = [list(map(int, input().split())) for _ in range(N)]
record.sort(reverse=True, key=lambda x:(x[1],x[2],x[3]))

for i in range(N):
  if record[i][0] == K:
    idx = i

for i in range(N):
  if record[idx][1:] == record[i][1:]:
    print(i+1)
    break