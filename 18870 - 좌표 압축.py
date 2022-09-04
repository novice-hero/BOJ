n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(set(x))

dic = {}
for i in range(len(x_sort)):
  dic[x_sort[i]] = i

for i in x:
  print(dic[i], end=' ')