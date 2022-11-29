n = int(input())
dp = [0]*36
dp[0],dp[1],dp[2] = 1,1,2

if n>2:
  for i in range(3, n+1):
    for j in range(i):
      dp[i] += dp[j]*dp[i-j-1]

print(dp[n])