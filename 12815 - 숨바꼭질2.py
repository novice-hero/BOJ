from collections import deque

n, k = map(int, input().split())
MAX_SIZE = 100001
check = [0]*MAX_SIZE

cnt = 0
q = deque()
q.append(n)
check[n] = 1

while q:
  cur = q.popleft()

  if cur == k:
    cnt += 1

  for i in [cur-1, cur+1, cur*2]:
    if 0 <= i < MAX_SIZE:
      if check[i] >= check[cur]+1 or check[i] == 0:
        check[i] = check[cur]+1
        q.append(i)

print(check[k]-1)
print(cnt)