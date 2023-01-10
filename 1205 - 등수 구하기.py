N, newScore, P = map(int, input().split())
if N == 0:
  print(1)
else:
  rankList = list(map(int, input().split()))
  rankList.append(newScore)
  rankList.sort(reverse=True)
  idx = rankList.index(newScore) + 1

  if idx > P:
    print(-1)
  else:
    if N == P and rankList[-1] == newScore:
      print(-1)
    else:
      print(idx)