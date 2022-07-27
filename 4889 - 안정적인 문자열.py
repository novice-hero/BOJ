n = 0
while True:
  t = input()
  n+=1
  cnt = 0
  stack = []
  if '-' in t:
    break

  for s in list(t):
    if s=='{':
      stack.append(s)
    elif s=='}':
      if stack:
        stack.pop()
      elif not stack:
        stack.append('{')
        cnt+=1
  
  print('{}. {}'.format(n, len(stack)//2+cnt))
