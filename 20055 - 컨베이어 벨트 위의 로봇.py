from collections import deque
n,k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*(len(belt)//2))
answer = 1

while True:
  # 1단계
  belt.rotate(1)
  robot.rotate(1)
  robot[-1] = 0

  # 2단계
  if sum(robot):
    for i in range(-2, -n-1, -1):
      if robot[i] == 1 and robot[i+1] == 0 and belt[i+1-n] >= 1:
        robot[i] = 0
        robot[i+1] = 1
        belt[i+1-n] -= 1
    robot[-1] = 0

  # 3단계
  if robot[0] == 0 and belt[0] != 0:
    robot[0] = 1
    belt[0] -= 1

  # 4단계
  if belt.count(0) >= k:
    break
  answer+=1

print(answer)