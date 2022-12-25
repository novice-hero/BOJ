p, m = map(int, input().split())
room = []
for _ in range(p):
  level, name = input().split()
  level = int(level)

  if len(room) == 0:
    room.append([[level, name]]);
  else:
    flag = False
    for r in room:
      if len(r) == m:
        continue
      if level <= r[0][0]+10 and level >= r[0][0]-10:
        r.append([level, name])
        flag = True
        break
    if not flag:
      room.append([[level, name]])

for res in room:
  temp = sorted(res, key=lambda x:x[1])
  if len(res) == m:
    print("Started!")
    for t in temp:
      print(*t)
  else:
    print('Waiting!')
    for t in temp:
      print(*t)