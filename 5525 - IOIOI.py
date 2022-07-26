N = int(input())
M = int(input())
S = input()
answer = 0
cnt = 0
stack = []

for i in range(M):
  if S[i] == 'I':
    stack.append(i)

for i in range(len(stack)-1):
  if stack[i+1]-stack[i] == 2:
    cnt+=1
  else:
    cnt = 0
  if cnt >= N:
    answer+=1

print(answer)