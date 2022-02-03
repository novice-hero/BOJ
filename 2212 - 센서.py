n = int(input())
k = int(input())
censor = list(map(int, input().split()))
censor.sort()

if k >= n:
    print(0)
else:
    censor_dt = []
    for i in range(len(censor)-1):
        censor_dt.append(abs(censor[i]-censor[i+1]))
    censor_dt.sort()

    for _ in range(k-1):
        censor_dt.pop()

    print(sum(censor_dt))