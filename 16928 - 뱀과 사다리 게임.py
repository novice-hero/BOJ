from collections import deque

board = [0] * 101
visited = [False] * 101
ladder, snake = {}, {}

n, m = map(int, input().split())
for _ in range(n):
  start, end = map(int, input().split())
  ladder[start] = end
for _ in range(m):
  start, end = map(int, input().split())
  snake[start] = end

q = deque([1])
while q:
  n = q.popleft()
  
  if n == 100:
    print(board[n])
    break

  for i in range(1, 7):
    num = n + i
    if num <= 100 and not visited[num]:
      if num in ladder.keys():
        num = ladder[num]
      if num in snake.keys():
        num = snake[num]
      if not visited[num]:
        visited[num] = True
        board[num] = board[n] + 1
        q.append(num)