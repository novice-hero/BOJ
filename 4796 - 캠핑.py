case = 1
while True:
  l,p,v = map(int, input().split())

  if l==0 and p==0 and v==0:
    exit()

  answer = (v//p)*l
  temp = v%p
  
  if temp>=l:
    answer+=l
  else:
    answer+=temp

  print("Case %d: %d" %(case, answer))
  case += 1