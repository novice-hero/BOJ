import heapq
import sys

def dijkstra(start):
  distance[start] = 0 # 자신의 비용은 0
  heapq.heappush(hq, [0, start]) # 시작 값 0으로 초기화

  while hq:
    cur_w, cur_node = heapq.heappop(hq)

    if distance[cur_node] < cur_w: # 현재 노드의 가중치가 현재 가중치보다 작으면 패스
      continue

    for next_node, weight in graph[cur_node]:
      # 현재 가중치 + 인접 노드의 가중치가 기존의 가중치 보다 작다면
      # 업데이트 하고 인접 노드와 더한 가중치를 넣는다
      if cur_w + weight < distance[next_node]:
        distance[next_node] = cur_w + weight
        heapq.heappush(hq, [cur_w + weight, next_node])

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
hq = []
for _ in range(E):
  u,v,w = map(int, input().split())
  graph[u].append([v,w])

dijkstra(K)
for i in distance[1:]:
  print(i if i!= INF else 'INF')