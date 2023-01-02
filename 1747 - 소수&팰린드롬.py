N = int(input())

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n%i == 0:
      return False
  return True

def isPalindrome(num):
  temp = list(str(num))
  mid = len(temp)//2
  temp = ['x'] + temp[0:]
  for j in range(1, mid+1):
    if temp[j] != temp[-j]:
      return False
  return True

while True:
  if isPrime(N) and isPalindrome(N):
    print(N)
    break
  N += 1