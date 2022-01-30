n = int(input())
nums = list(map(int, input().split()))
nums.sort()
idx = len(nums) // 2 - 1

print(nums[idx])