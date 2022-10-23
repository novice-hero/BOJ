n, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
start, end = 0, 0
count = [0]*(max(nums)+1)

while end < n:
  if count[nums[end]] < k:
    count[nums[end]] += 1
    end += 1
  else:
    count[nums[start]] -= 1
    start += 1
  answer = max(answer, end-start)

print(answer)