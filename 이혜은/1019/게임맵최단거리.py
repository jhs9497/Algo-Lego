from collections import deque


def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    maps[0][0] = '1'
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    def bfs(r, c):
        q = deque()
        q.append([r, c])
        while q:
            r, c = q.popleft()
            for di in range(4):
                nr = r + dr[di]
                nc = c + dc[di]
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if maps[nr][nc] == 0:
                    continue
                if maps[nr][nc] == 1:
                    maps[nr][nc] = str(int(maps[r][c]) + 1)
                    q.append([nr, nc])
                    continue
                if int(maps[nr][nc]) <= int(maps[r][c]) + 1:
                    continue
                else:
                    maps[nr][nc] = str(int(maps[r][c]) + 1)
                    q.append([nr, nc])
                    continue
                
    
    bfs(0, 0)
    
    print(maps)
    if maps[N-1][M-1] != 1:
        answer = int(maps[N-1][M-1])
    else:
        answer = -1
        
    return answer