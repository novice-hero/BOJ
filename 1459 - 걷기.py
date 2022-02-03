x, y, w, s = list(map(int, input().split()))
# 평행
temp1 = (x + y) * w
# 대각선, x+y가 짝수
if (x + y) % 2 == 0:
    temp2 = max(x, y) * s
# 대각선, x+y가 홀수
else:
    temp2 = (max(x, y) - 1) * s + w
# 평행 + 대각선
temp3 = (min(x, y) * s) + (abs(x - y) * w)

print(min(temp1,temp2,temp3))
