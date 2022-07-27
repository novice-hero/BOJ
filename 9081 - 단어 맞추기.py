def nextPermutation(s):
  n1 = -1
  s=list(s)
  for i in range(len(s)-1):
    if s[i] < s[i+1]:
      n1 = i
  
  if n1 == -1:
    return False

  for i in range(len(s)-1, -1, -1):
    if s[n1] < s[i]:
      n2 = i
      break

  s[n1],s[n2] = s[n2],s[n1]

  return "".join(s[:n1+1]+s[n1+1:][::-1])

t = int(input())
for _ in range(t):
  word = input()
  if nextPermutation(word)==False:
    print(word)
  else:
    print(nextPermutation(word))
