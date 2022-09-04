n = int(input())

max_dp = [0]*3
min_dp = [0]*3
max_t = [0]*3
min_t = [0]*3

for _ in range(n):
  a, b, c = map(int, input().split())
  for i in range(3):
    if i == 0:
      max_t[i] = a + max(max_dp[i], max_dp[i+1])
      min_t[i] = a + min(min_dp[i], min_dp[i+1])
    elif i == 1:
      max_t[i] = b + max(max_dp[i-1], max_dp[i], max_dp[i+1])
      min_t[i] = b + min(min_dp[i-1], min_dp[i], min_dp[i+1])
    else:
      max_t[i] = c + max(max_dp[i-1], max_dp[i])
      min_t[i] = c + min(min_dp[i-1], min_dp[i])
  for i in range(3):
    max_dp[i] = max_t[i]
    min_dp[i] = min_t[i]

print(max(max_dp), min(min_dp))