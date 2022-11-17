for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    xLeft = max(x1, x3)
    xRight = min(x2, x4)
    yBottom = max(y1, y3)
    yTop = min(y2, y4)

    xd = xRight - xLeft
    yd = yTop - yBottom

    if xd > 0 and yd > 0:
        print('a')
    elif xd < 0 or yd < 0:
        print('d')
    elif xd == 0 and yd == 0:
        print('c')
    else:
        print('b')
