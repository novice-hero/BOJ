n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num = sorted(num)
for i in num:
    print(i)
