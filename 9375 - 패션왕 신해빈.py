t = int(input())

for _ in range(t):
  dic = {}
  n = int(input())
  for _ in range(n):
    name, kind = input().split()
    if kind in dic:
      dic[kind] += 1
    else:
      dic[kind] = 1  
  answer = 1
  arr = dic.values()
  for i in arr:
    answer *= (i+1)
  
  print(answer - 1)