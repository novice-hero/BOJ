t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    high = stocks[-1]
    answer = 0
    for i in range(n-1, -1, -1):
        if high > stocks[i]:
            answer += high - stocks[i]
        else:
            high = stocks[i]
    print(answer)