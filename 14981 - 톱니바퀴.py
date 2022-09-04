from collections import deque

def checkRight(start, r):
  if start>4 or gear[start-1][2] == gear[start][6]:
    return
  
  if gear[start-1][2] != gear[start][6]:
    checkRight(start+1, -r)
    gear[start].rotate(r)

def checkLeft(start, r):
  if start<1 or gear[start][2] == gear[start+1][6]:
    return
  
  if gear[start][2] != gear[start+1][6]:
    checkLeft(start-1, -r)
    gear[start].rotate(r)

gear = {}
for i in range(1,5):
  gear[i] = deque(list(input()))

for _ in range(int(input())):
  n, r = map(int, input().split())
  checkLeft(n-1, -r)
  checkRight(n+1, -r)
  gear[n].rotate(r)

answer = 0
for i in range(4):
  answer+=(2**i) * int(gear[i+1][0])

print(answer)