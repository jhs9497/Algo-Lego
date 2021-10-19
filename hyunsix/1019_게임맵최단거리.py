from collections import deque

def BFS(maps, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((0, 0))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if maps[new_x][new_y] == 1:
                    if new_x == 0 and new_y == 0:
                        continue
                    else:
                        maps[new_x][new_y] = maps[x][y] + 1
                        Q.append((new_x, new_y))

                elif maps[new_x][new_y] > 1:
                    if maps[new_x][new_y] > maps[x][y] + 1:
                        maps[new_x][new_y] = maps[x][y] + 1
                        Q.append((new_x, new_y))
    return


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    BFS(maps, N, M)
    # for i in range(len(maps)):
    #     print(*maps[i])

    if maps[N - 1][M - 1] > 1:
        return maps[N - 1][M - 1]
    else:
        return -1