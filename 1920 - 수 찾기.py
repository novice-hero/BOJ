n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

def search(target):
  start = 0
  end = n-1
  while start <= end:
    mid = (start+end)//2
    if a[mid] == target:
      return True
    elif a[mid] > target:
      end = mid - 1
    else:
      start = mid + 1

for i in range(m):
  if search(nums[i]):
    print(1)
  else:
    print(0)