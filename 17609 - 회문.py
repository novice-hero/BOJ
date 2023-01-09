def checkPalindrome(s):
  left, right = 0, len(s)-1
  while left <= right:
    if s[left] == s[right]:
      left+=1
      right-=1
    else:
      return False
  return True

def checkPseudoPalindromeRight(s):
  left, right = 0, len(s)-1
  flag = 0
  while left < right:
    if s[left] == s[right]:
      left+=1
      right-=1
    else:
      right-=1
      flag+=1
  if flag == 1:
    return True
  else:
    return False

def checkPseudoPalindromeLeft(s):
  left, right = 0, len(s)-1
  flag = 0
  while left < right:
    if s[left] == s[right]:
      left+=1
      right-=1
    else:
      left+=1
      flag+=1
  if flag == 1:
    return True
  else:
    return False

N = int(input())
for _ in range(N):
  word = input()
  if checkPalindrome(word):
    print(0)
  elif checkPseudoPalindromeLeft(word) or checkPseudoPalindromeRight(word):
    print(1)
  else:
    print(2)