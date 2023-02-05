N = int(input())
stone = list(map(int, input().split()))
stone1, stone2 = [], []

for s in stone:
  if s == 2: stone1.append(-1)
  else: stone1.append(1)

for s in stone:
  if s == 1: stone2.append(-1)
  else: stone2.append(1)

def solve(arr):
  answer, prev = 0, 0
  for a in arr:
    prev += a
    prev = max(0, prev)
    answer = max(answer, prev)
  return answer

print(max(solve(stone1), solve(stone2)))