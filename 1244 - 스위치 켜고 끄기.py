switch_num = int(input())
switch_arr = [False] + list(map(int, input().split()))
stu_num = int(input())

def change(n):
  if switch_arr[n]==0: 
    switch_arr[n]=1
  else: 
    switch_arr[n]=0
  return

for _ in range(stu_num):
  sex, num = map(int, input().split())
  if sex == 1:
    for i in range(num, switch_num+1, num):
        change(i)
  
  else:
    change(num)
    for k in range(switch_num//2):
      if num + k > switch_num or num - k < 1 : break
      if switch_arr[num + k] == switch_arr[num - k]:
        change(num + k)
        change(num - k)
      else:
        break


for i in range(1, switch_num+1):
  print(switch_arr[i], end=" ")
  if i % 20 == 0:
    print()