from copy import deepcopy

n = int(input())
honey = list(map(int, input().split()))
honeySum = deepcopy(honey)
answer = 0

for i in range(1, n):
  honeySum[i] += honeySum[i-1]

for i in range(1, n-1):
  answer = max(answer, 2*honeySum[-1]-honey[0]-honey[i]-honeySum[i])

for i in range(1, n-1):
  answer = max(answer, honeySum[-1]+honeySum[i-1]-honey[-1]-honey[i])

for i in range(1, n-1):
  answer = max(answer, honeySum[i]-honey[0]+honeySum[-1]-honey[-1]-honeySum[i-1])

print(answer)