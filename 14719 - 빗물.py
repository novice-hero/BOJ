h,w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
  left = max(block[:i])
  right = max(block[i+1:])
  minimal = min(left, right)

  if minimal > block[i]:
    answer += minimal - block[i]

print(answer)