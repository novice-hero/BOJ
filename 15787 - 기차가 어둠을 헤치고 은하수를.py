from collections import deque
N, M = map(int, input().split())
trains = [deque([0]*20) for _ in range(N)]
for _ in range(M):
  command = list(map(int, input().split()))
  if command[0] == 1:
    trains[command[1]-1][command[2]-1] = 1
  elif command[0] == 2:
    trains[command[1]-1][command[2]-1] = 0
  elif command[0] == 3:
    trains[command[1]-1].appendleft(0)
    trains[command[1]-1].pop()
  elif command[0] == 4:
    trains[command[1]-1].popleft()
    trains[command[1]-1].append(0)

answer = []
for t in trains:
  if t not in answer:
    answer.append(t)

print(len(answer))