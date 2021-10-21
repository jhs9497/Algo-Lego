from collections import deque
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 111111

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(i,j):
    cnt = 1
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1
    while queue:
        i, j = queue.popleft()
        di = [-1,1,0,0]
        dj = [0,0,-1,1]
        for n in range(4):
            new_i = i + di[n]
            new_j = j + dj[n]
            if 0<=new_i<N and 0<=new_j<M and visited[new_i][new_j] == 0:
                if arr[new_i][new_j] == 1:
                    queue.append([new_i,new_j])
                    # if visited[new_i][new_j] < visited[i][j] + 1:
                    visited[new_i][new_j] = visited[i][j] + 1

bfs(0,0)
print(visited[N-1][M-1])
