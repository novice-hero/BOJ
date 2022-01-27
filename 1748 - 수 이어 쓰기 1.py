n = int(input())
length = len(str(n))
answer = 0
for i in range(length - 1):
    answer += 9 * 10 ** i * (i + 1)

print(answer + (n - 10 ** (length - 1) + 1) * length)
