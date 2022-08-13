n = int(input())
ballon = list(map(int, input().split()))
shot = 0

while True:
  maxIdx = ballon.index(max(ballon))
  maxBallon = max(ballon)

  if maxBallon == 0: break

  for i in range(maxIdx, len(ballon)):
    if ballon[i] == maxBallon:
      maxBallon -= 1
      ballon[i] = 0
  shot+=1

print(shot)