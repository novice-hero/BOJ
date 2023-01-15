N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

prev_start, prev_end = lines[0][0], lines[0][1]
answer = 0

for i in range(1, N):
  cur_start, cur_end = lines[i]
  if prev_end >= cur_end:
    continue
  elif cur_start <= prev_end <= cur_end:
    prev_end = cur_end
  else:
    answer += abs(prev_end - prev_start)
    prev_start, prev_end = cur_start, cur_end

answer += abs(prev_end - prev_start)
print(answer)