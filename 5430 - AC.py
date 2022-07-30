from collections import deque
t = int(input())

for _ in range(t):
  p = input()
  n = int(input())
  arr = input()
  dq = deque(arr[1:-1].split(","))
  flag = False

  if n==0:
    dq = deque()
  
  reverse = 0
  for s in p:
    if s == 'R':
      reverse += 1
    elif s == 'D':
      if len(dq) == 0:
        print('error')
        flag = True
        break
      else:
        if reverse%2==0:
          dq.popleft()
        else:
          dq.pop()
  
  if flag:
    continue
  else:
    if reverse % 2 == 0:
      print('[' + ",".join(dq) + ']')
    else:
      dq.reverse()
      print('[' + ",".join(dq) + ']')

