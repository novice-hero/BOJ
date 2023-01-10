def check(nums):
  for i in range(1, len(nums)+1):
    if nums[-(i*2):-i] == nums[-i:]:
      return False
  return True

def requr(idx, nums):
  if idx == N:
    print(nums)
    exit()
  
  for i in '123':
    if check(nums+i):
      requr(idx+1, nums+i)

N = int(input())
requr(1, '1')
