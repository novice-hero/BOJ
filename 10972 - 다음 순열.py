n = int(input())
number = list(map(int, input().split()))

for i in range(n-1, 0 , -1):
    if number[i-1] < number[i]:
        for j in range(n-1,0,-1):
            if number[i-1] < number[j]:
                number[i-1],number[j] = number[j],number[i-1]
                answer = number[:i] + sorted(number[i:])
                print(*answer)
                exit()

print(-1)