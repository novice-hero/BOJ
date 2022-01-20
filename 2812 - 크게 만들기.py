n, k = map(int, input().split())
s = input()

stack = []

for i in s:
    while stack and i > stack[-1]:
        if k > 0:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(i)
if k > 0:
    for i in range(k):
        stack.pop()

print(''.join(stack))
