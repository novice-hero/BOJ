import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
  x = int(sys.stdin.readline())
  if x==0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap)*-1)
  else:
    heapq.heappush(heap, -x)