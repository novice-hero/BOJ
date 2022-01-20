t = int(input())
for _ in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    height.sort()

    one, two = [], []
    one = [height[x] for x in range(len(height)) if x % 2 == 0]
    two = [height[x] for x in range(len(height)) if x % 2 == 1]
    two.sort(reverse=True)
    plus = one + two

    temp = []
    for i in range(len(plus)-1):
        temp.append(abs(plus[i]-plus[i+1]))

    print(max(temp))
