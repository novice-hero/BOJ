import sys

K, L = map(int, sys.stdin.readline().split())
stuList = {}
for i in range(L):
    stu_num = sys.stdin.readline().rstrip()
    stuList[stu_num] = i

cnt = 0
for x in sorted(stuList.items(), key=lambda x: x[1]):
    cnt += 1
    if cnt > K:
        break
    print(x[0])
