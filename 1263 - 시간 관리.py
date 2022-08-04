n = int(input())
time = []
for _ in range(n):
  time.append(list(map(int, input().split())))
time.sort(key=lambda x:x[1])

answer = 0
while True:
  temp = answer
  for t in time:
    if temp+t[0] <= t[1]:
      temp+=t[0]
    else:
      print(answer-1)
      exit()
  answer+=1
