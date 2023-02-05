def dfs(T):
  if T==S:
    return True 
  if len(T) > 1 and T[-1]=='A' and dfs(T[:-1]):
    return True
  if len(T) > 1 and T[0]=='B' and dfs(T[1:][::-1]):
    return True
  
  return False

S = input()
T = input()
if dfs(T):
  print(1)
else:
  print(0)