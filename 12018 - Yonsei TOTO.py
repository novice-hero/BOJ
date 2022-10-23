n, m = map(int, input().split())
temp = []
Sum ,answer = 0, 0

for _ in range(n):
  p, l = map(int, input().split())
  mList = list(map(int, input().split()))
  mList.sort(reverse=True)
  
  if len(mList) < l:
    temp.append(1)
  else:
    temp.append(mList[l-1])

temp.sort()

for t in temp:
  Sum += t
  answer += 1

  if Sum > m:
    answer -= 1
    break

print(answer)