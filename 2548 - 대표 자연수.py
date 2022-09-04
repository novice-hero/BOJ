n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if len(nums)%2==0:
  idx = len(nums) // 2 - 1
else:
  idx = len(nums) // 2

print(nums[idx])