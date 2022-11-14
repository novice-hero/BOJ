N = int(input())
arr = []
total, maxIdx, maxV, maxL = 0, 0, 0, 0
for _ in range(N):
  L, H = map(int, input().split())
  if maxV < H:
    maxV = H
    maxIdx = L
  if maxL < L:
    maxL = L
  arr.append([L,H])

pList = [0]*(maxL+1)
for l,h in arr:
  pList[l] = h

temp = 0
for i in range(maxIdx+1):
  if temp < pList[i]:
    temp = pList[i]
  total += temp
temp = 0
for i in range(maxL, maxIdx, -1):
  if temp < pList[i]:
    temp = pList[i]
  total += temp

print(total)