n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxN = -999999999
minN = +999999999

def dfs(depth, total, plus, minus, mul, div):
  global maxN, minN

  if depth == n:
    maxN = max(total, maxN)
    minN = min(total, minN)
    return
  
  if plus:
    dfs(depth+1, total+num[depth], plus-1, minus, mul, div)
  if minus:
    dfs(depth+1, total-num[depth], plus, minus-1, mul, div)
  if mul:
    dfs(depth+1, total*num[depth], plus, minus, mul-1, div)
  if div:
    dfs(depth+1, int(total/num[depth]), plus, minus, mul, div-1)

dfs(1, num[0], oper[0], oper[1], oper[2], oper[3])

print(maxN)
print(minN)
