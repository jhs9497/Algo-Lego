T = int(input())
def BFS(x, y, field, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = []
    Q.append((x,y))
    while Q:
        x, y = Q.pop(0)
        field[x][y] = 0
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if field[new_x][new_y] == 1:
                    Q.append((new_x, new_y))
                    field[new_x][new_y] = 0
    return

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        field[j][i] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                BFS(i, j, field, N, M)
                count += 1

    print(count)