import heapq
n = int(input())
room = []
for _ in range(n):
  room.append(list(map(int, input().split())))
room = sorted(room, key=lambda x:(x[0], x[1]-x[0]))
conference = [-1]

for start, end in room:
  if conference and conference[0] <= start:
    heapq.heappop(conference)
  heapq.heappush(conference, end)

print(len(conference))