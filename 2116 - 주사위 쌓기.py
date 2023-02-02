n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

def findMax(dice, num):
  for idx in range(6): # 밑 주사위의 윗면의 숫자의 인덱스 찾기
    if dice[idx] == num:
      break
  # 윗 주사위의 밑면이 되어야 하는 숫자를 찾아서 넘겨주기 ( 1=6, 2=4, 3=5 )
  if idx == 0:
    return [dice[5], max(dice[1], dice[2], dice[3],dice[4])]
  elif idx == 1:
    return [dice[3], max(dice[0], dice[2], dice[4],dice[5])]
  elif idx == 2:
    return [dice[4], max(dice[0], dice[1], dice[3],dice[5])]
  elif idx == 3:
    return [dice[1], max(dice[0], dice[2], dice[4],dice[5])]
  elif idx == 4:
    return [dice[2], max(dice[0], dice[1], dice[3],dice[5])]
  elif idx == 5:
    return [dice[0], max(dice[1], dice[2], dice[3],dice[4])]

answer = 0
for i in range(6):
  # 첫번째 주사위의 모든 면을 해보기
  next_val, total = findMax(dices[0], dices[0][i])
  for j in range(1, n):
    temp1, temp2 = findMax(dices[j], next_val)
    next_val = temp1
    total += temp2
  answer = max(answer, total) # 최댓값 구하기

print(answer)