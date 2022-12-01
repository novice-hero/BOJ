N = int(input())
room = [[0]*N for _ in range(N)]
dr, dc = [1,-1,0,0], [0,0,-1,1]
dic = {}
answer = 0

for _ in range(N**2):
  nums = list(map(int, input().split()))
  stu, stu_list = nums[0], nums[1:]
  dic[stu] = stu_list
  temp = []
  for i in range(N):
    for j in range(N):
      if room[i][j] == 0:
        favorite, empty = 0, 0
        for k in range(4):
          nr = i + dr[k]
          nc = j + dc[k]
          if 0<=nr<N and 0<=nc<N:
            if room[nr][nc] in stu_list:
              favorite += 1
            if room[nr][nc] == 0:
              empty += 1
        temp.append([favorite, empty, i, j])
  temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
  room[temp[0][2]][temp[0][3]] = stu

for i in range(N):
  for j in range(N):
    cnt = 0
    for k in range(4):
      nr = i + dr[k]
      nc = j + dc[k]
      if 0<=nr<N and 0<=nc<N:
        if room[nr][nc] in dic[room[i][j]]:
          cnt += 1
    if cnt == 1:
      answer += 1
    elif cnt == 2:
      answer += 10
    elif cnt == 3:
      answer += 100
    elif cnt == 4:
      answer += 1000

print(answer)