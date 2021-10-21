from collections import deque
answer = 0
N, M = map(int,input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
print(visited[3][1])

cnt = 0
def bfs(arr, i,j, visited,cnt):
    queue = deque([[i,j]])
    # 현재노드 방문처리
    visited[i][j] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        i, j = queue.popleft()
        print(i,j)
        # 상하좌우 체크
        di = [-1,1,0,0]
        dj = [0,0,-1,1]
        for n in range(4):
            new_i = i + di[n]
            new_j = j + dj[n]

            # 인덱스 체크
            if 0<=new_i<N and 0<=new_j<M and visited[new_i][new_j] == False:
                if arr[new_i][new_j] == 0:
                    # 아직 방문하지 않은 인접한 원소들 큐에 삽입
                    queue.append([new_i,new_j])
                    visited[new_i][new_j] = True
    # 목표
    cnt += 1
    return cnt

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            answer += bfs(arr,i,j,visited,cnt)

print(visited)
print(answer)

# 4 5
# 00110
# 00011
# 11111
# 00000