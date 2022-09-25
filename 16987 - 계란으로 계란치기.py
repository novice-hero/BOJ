n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def check(eggs):
  count = 0
  for egg in eggs:
    if egg[0] <= 0:
      count += 1
  return count

def dfs(idx, eggs):
  global answer
  if idx == n:
    answer = max(answer, check(eggs))
    return
  
  if eggs[idx][0] <= 0:
    dfs(idx+1, eggs)
  else:
    flag = True
    for i in range(n):
      if idx != i and eggs[i][0] > 0:
        flag = False
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        dfs(idx+1, eggs)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]
    
    if flag:
      dfs(n, eggs)

dfs(0, eggs)
print(answer)
