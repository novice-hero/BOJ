def dfs(cnt, num):
  if cnt == 1:
    arr.add(str(num))
    return
  for i in range(N):
    for j in range(i+1, N):
      visited[i],visited[j] = 1,1
      dfs(cnt+1, A[i]*A[j])
      visited[i],visited[j] = 0,0

T = int(input())
for tc in range(1, T+1):
  N = int(input())
  A = list(map(int, input().split()))
  visited = [0]*N
  arr = set()
  answer = []

  if N == 1:
    arr.add(str(A[0]))
  else:
    dfs(0, 0)
  arr = list(arr)

  for a in arr:
    flag = True
    
    for i in range(len(a)-1):
      if a[i] > a[i+1]:
        flag = False
    
    if flag:
      temp = int(a)
      if temp > 9:
        answer.append(temp)
  
  if len(answer) == 0:
    print(f'#{tc} {-1}')
  else:
    print(f'#{tc} {max(answer)}')