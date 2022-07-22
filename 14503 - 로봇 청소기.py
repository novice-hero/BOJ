N,M = map(int,input().split())
graph = []
visited = [[0] * M for _ in range(N)]
x,y,d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(N):
    graph.append(list(map(int,input().split())))

visited[x][y] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        nx = x + dx[(d+3)%4]
        ny = y + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x = nx
                y = ny
                flag = 1
                break
    if flag == 0: 
        if graph[x-dx[d]][y-dy[d]] == 1: 
            print(cnt)
            break
        else:
            x,y = x-dx[d],y-dy[d]