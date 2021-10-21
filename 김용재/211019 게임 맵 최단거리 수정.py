from collections import deque


def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]

    bfs(maps, 0, 0, visited)
    answer = visited[N - 1][M - 1]
    if answer == 0:
        return -1
    return answer


def bfs(maps, i, j, visited):
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        i, j = queue.popleft()

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for n in range(4):
            new_i = i + di[n]
            new_j = j + dj[n]
            if 0 <= new_i < N and 0 <= new_j < M and visited[new_i][new_j] == 0:
                if maps[new_i][new_j] == 1:
                    visited[new_i][new_j] = visited[i][j] + 1
                    queue.append([new_i, new_j])




