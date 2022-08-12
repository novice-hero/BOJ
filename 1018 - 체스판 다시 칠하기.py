n,m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = []

def check88(a,b):
  global board, answer
  cnt1 = 0
  cnt2 = 0
  for i in range(a, a+8):
    for j in range(b, b+8):
      if (i+j)%2 == 0:
        if board[i][j] != 'W': cnt1+=1
        if board[i][j] != 'B': cnt2+=1
      else:
        if board[i][j] != 'B': cnt1+=1
        if board[i][j] != 'W': cnt2+=1
        
  answer.append(cnt1)
  answer.append(cnt2)

for i in range(n-7):
  for j in range(m-7):
    check88(i,j)

print(min(answer))