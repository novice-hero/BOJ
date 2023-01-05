N = int(input())
room = [input() for _ in range(N)]
width, height = 0, 0

for i in range(N):
  check = 0
  for j in range(N):
    if room[i][j] == '.':
      check += 1
    else:
      if check > 1:
        width += 1
        check = 0
      else: check = 0
  if check > 1:
    width += 1

for i in range(N):
  check = 0
  for j in range(N):
    if room[j][i] == '.':
      check += 1
    else: 
      if check > 1:
        height += 1
        check = 0
      else: check = 0
  if check > 1:
    height += 1

print(width, height)