import re

n = int(input())
f, b = input().split('*')
p = re.compile(f + '.*' + b + '+')

for _ in range(n):
    name = input()
    a = p.search(name)
    if a and a.group() == name:
        print('DA')
    else:
        print('NE')