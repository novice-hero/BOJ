import heapq
move = [[1,0],[-1,0],[0,-1],[0,1]]
t = 1
INF = 1e9

def dij():
  distance, q = [[INF]*n for _ in range(n)], []
  distance[0][0] = 0
  heapq.heappush(q, [cave[0][0], 0, 0])

  while q:
    w, r, c = heapq.heappop(q)
    if r==n-1 and c==n-1:
      print('Problem {}: {}'.format(t, distance[-1][-1]))
      return
    for i in range(4):
      nr = r + move[i][0]
      nc = c + move[i][1]
      if 0<=nr<n and 0<=nc<n:
        nw = w + cave[nr][nc]
        if nw < distance[nr][nc]:
          distance[nr][nc] = nw
          heapq.heappush(q, [nw, nr, nc])

while True:
  n = int(input())
  if n==0:
    break
  cave = [list(map(int, input().split())) for _ in range(n)]
  bfs()
  t += 1