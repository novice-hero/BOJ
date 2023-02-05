import sys

def check():
  for i in range(n-1):
    if phoneNumbers[i] in phoneNumbers[i+1][:len(phoneNumbers[i+1])-1]:
      return False
  return True

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  phoneNumbers = [sys.stdin.readline().rstrip() for _ in range(n)]
  phoneNumbers.sort()

  if check():
    print('YES')
  else:
    print('NO')