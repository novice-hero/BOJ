# PyPy3로 해야 시간 초과가 안남
n = int(input())
board = [list(input()) for _ in range(n)]

def check(board):
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(len(board) - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        cnt = 1
        for j in range(len(board) - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt


answer = 0
for i in range(n):
    for j in range(len(board) - 1):
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        cnt = check(board)
        answer = max(cnt, answer)
        board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]

    for j in range(len(board) - 1):
        board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
        cnt = check(board)
        answer = max(cnt, answer)
        board[j + 1][i], board[j][i] = board[j][i], board[j + 1][i]

print(answer)
