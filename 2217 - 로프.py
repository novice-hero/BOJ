N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
answer = []

for i in range(len(rope)):
  answer.append(rope[i]*(i+1))

print(max(answer))