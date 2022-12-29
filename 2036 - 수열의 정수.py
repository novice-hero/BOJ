n = int(input())
positive = []
negative = []
one = []
answer = 0
for _ in range(n):
  temp = int(input())
  if temp == 1:
    one.append(temp)
  elif temp <= 0:
    negative.append(temp)
  else:
    positive.append(temp)
positive.sort(reverse=True)
negative.sort()

if len(positive)%2==0:
  for i in range(0, len(positive), 2):
    answer += positive[i]*positive[i+1]
else:
  answer += positive.pop()
  for i in range(0, len(positive), 2):
    answer += positive[i]*positive[i+1]

if len(negative)%2==0:
  for i in range(0, len(negative), 2):
    answer += negative[i]*negative[i+1]
else:
  answer += negative.pop()
  for i in range(0, len(negative), 2):
    answer += negative[i]*negative[i+1]
answer += sum(one)

print(answer)