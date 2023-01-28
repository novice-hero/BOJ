import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
nums = [0]
for n in range(N):
  nums.append(nums[-1]+arr[n])

for _ in range(M):
  i, j = map(int, input().split())
  print(nums[j]-nums[i-1])