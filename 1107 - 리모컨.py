import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
button = list(map(int, input().split()))
min_cnt = abs(100 - n)

for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in button:
            break
        elif j == len(i) - 1:
            min_cnt = min(min_cnt, abs(int(i) - n) + len(i))

print(min_cnt)
