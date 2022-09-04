import sys
input = sys.stdin.readline

m = int(input())
S = set()
for _ in range(m):
  words = input().split()
  if len(words) == 1:
    if words[0] == 'all':
      S = set([i for i in range(1,21)])
    else:
      S = set()

  else:
    x = int(words[1])
    if words[0] == 'add':
      S.add(x)
    
    elif words[0] == 'remove':
      S.discard(x)
    
    elif words[0] == 'check':
      if x in S:
        print(1)
      else:
        print(0)
    
    elif words[0] == 'toggle':
      if x in S:
        S.discard(x)
      else:
        S.add(x)