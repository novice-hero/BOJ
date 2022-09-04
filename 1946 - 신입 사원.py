import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  arr = []
  cnt = 1
  for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
  arr.sort(key=lambda x:x[0])
  
  temp = 0
  for i in range(1, len(arr)):
    if arr[temp][1] > arr[i][1]:
      temp = i
      cnt += 1

  print(cnt)