a,b = map(int, input().split())
temp = []
temp2 = []
cnt = 1;
for _ in range(b):
  for _ in range(cnt):
    if len(temp)+len(temp2) == b:
      break
    elif len(temp2)<a-1:
      temp2.append(cnt)
    else: 
      temp.append(cnt)
  cnt+=1

print(sum(temp))