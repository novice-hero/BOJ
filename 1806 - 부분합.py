n,s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0,0
sumN = 0
minLen = 100000

while True:
  if sumN >= s:
    minLen = min(minLen, right-left)
    sumN-=nums[left]
    left+=1
  elif right == n:
    break
  else:
    sumN+=nums[right]
    right+=1

if sum(nums) < s:
  print(0)
else:
  print(minLen)