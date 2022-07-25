from sys import stdin
input = stdin.readline

treeDic = {}
cnt = 0

while True:
  tree = input().rstrip()
  if tree=="":
    break;
  if tree in treeDic:
    treeDic[tree] += 1
  else:
    treeDic[tree] = 1
  cnt += 1

treeName = sorted(treeDic)
for t in treeName:
  print('%s %.4f' %(t, treeDic[t]/cnt*100))