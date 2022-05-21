from collections import deque

s = int(input())
visited = [[False]*(s+1) for _ in range(s+1)]
q = deque()
q.append([1,0,0])
visited[1][0] = True

while q:
  scr, clip, cnt = q.popleft()

  if scr == s:
    print(cnt)
    break

  if scr != clip and not visited[scr][scr]:
    visited[scr][scr] = True
    q.append([scr,scr,cnt+1])
  
  if scr+clip <= s and clip!=0 and not visited[scr+clip][clip]:
    visited[scr+clip][clip] = True
    q.append([scr+clip, clip, cnt+1])

  if scr!=0 and not visited[scr-1][clip]:
    visited[scr-1][clip] = True
    q.append([scr-1, clip, cnt+1])