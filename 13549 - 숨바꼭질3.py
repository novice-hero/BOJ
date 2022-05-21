from collections import deque

MAX_SIZE = 100001
n,k = map(int, input().split())
arr = [0]*MAX_SIZE

q = deque()
q.append(n)
arr[n] = 1

while q:
  cur = q.popleft()

  if cur == k:
    print(arr[k]-1)
    break

  if 0<=cur*2<MAX_SIZE and arr[cur*2] == 0:
    arr[cur*2] = arr[cur]
    q.appendleft(cur*2)
  if 0<=cur-1<MAX_SIZE and arr[cur-1] == 0:
    arr[cur-1] = arr[cur] + 1
    q.append(cur-1)
  if 0<=cur+1<MAX_SIZE and arr[cur+1] == 0:
    arr[cur+1] = arr[cur] + 1
    q.append(cur+1)

