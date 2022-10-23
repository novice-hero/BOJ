n = int(input())
loss=  list(map(int, input().split()))
loss.sort()
result = []

if len(loss) % 2 == 1:
  result.append(loss.pop())
  for i in range(0, len(loss)//2):
    result.append(loss[i]+loss[-i-1])
  print(max(result))
  exit()

else:
  for i in range(0, len(loss)//2):
    result.append(loss[i]+loss[-i-1])
  print(max(result))
  exit()