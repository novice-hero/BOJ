h,w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

left = 0
right = w-1
maxL = -1
maxR = -1

while left < right:
  maxL = max(maxL, block[left])
  maxR = max(maxR, block[right])

  if maxL > maxR:
    answer += maxR - block[right]
    right-=1

  elif maxL < maxR:
    answer += maxL - block[left]
    left+=1

print(answer)