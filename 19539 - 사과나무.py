N = int(input())
height = list(map(int, input().split()))
height_sum = sum(height)
height_div = height_sum // 3

if height_sum % 3 != 0:
  print("NO")
else:
  for h in height:
    height_div -= h//2
  if height_div > 0:
    print("NO")
  else:
    print("YES")