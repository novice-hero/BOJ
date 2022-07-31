import copy
T = int(input())

def dfs(arr, n):
  if len(arr) == n:
    op_list.append(copy.deepcopy(arr))
    return
  
  arr.append(" ")
  dfs(arr, n)
  arr.pop()

  arr.append("+")
  dfs(arr, n)
  arr.pop()

  arr.append("-")
  dfs(arr, n)
  arr.pop()


for _ in range(T):
  n = int(input())
  op_list = []
  nums = [i+1 for i in range(n)]
  dfs([], n-1)

  for op in op_list:
    s = ''
    for i in range(len(nums)-1):
      s += str(nums[i])+op[i]
    s += str(nums[-1])

    if eval(s.replace(" ","")) == 0:
      print(s)
  print()