n,m = map(int, input().split())
arr = list(map(int, input().split()))

def divide(num):
  max_num = arr[0]
  min_num = arr[0]
  cnt = 1
  for i in range(1, n):
    max_num = max(max_num, arr[i])
    min_num = min(min_num, arr[i])
    if max_num - min_num > num:
      cnt += 1
      max_num = arr[i]
      min_num = arr[i]
  return cnt

start = 0
end = max(arr)
answer = 0

while start <= end:
  mid = (start+end) // 2
  if divide(mid) <= m:
    end = mid - 1
    answer = mid
  else:
    start = mid + 1

print(answer)