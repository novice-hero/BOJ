N = int(input())
day = []
money = []
for _ in range(N):
  a,b = map(int, input().split())
  day.append(a)
  money.append(b)
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + day[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], money[i] + dp[i + day[i]])
    
print(dp[0])