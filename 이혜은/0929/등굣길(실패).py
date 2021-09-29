def solution(m, n, puddles):
    answer = 0
    
    dr = [0, 1]
    dc = [1, 0]
    
    dis = [[0x9999999]*(m) for _ in range(n)]
    ans = [[0]*(m) for _ in range(n)]
    
    dis[0][0] = 0
    ans[0][0] = 1
    
    for puddle in puddles:
        c, r = puddle
        dis[r-1][c-1] = -1
    
    def update_dis(r, c):
            
        for di in range(2):
            nr = r + dr[di]
            nc = c + dc[di]
            if 0 > nr or nr >= n or 0 > nc or nc >= m:
                continue
            if dis[nr][nc] == -1:
                continue
            if 1 + dis[r][c] > dis[nr][nc]:
                continue
            if 1 + dis[r][c] < dis[nr][nc]:
                dis[nr][nc] = 1 + dis[r][c]
                ans[nr][nc] = 1
            elif 1 + dis[r][c] == dis[nr][nc]:
                if nr == 0:
                    ans[nr][nc] = ans[nr][nc-1]
                elif nc == 0:
                    ans[nr][nc] = ans[nr-1][nc]
                else:
                    ans[nr][nc] = ans[nr][nc-1]+ans[nr-1][nc]
            update_dis(nr, nc)
            
    update_dis(0, 0)
    return (ans[n-2][m-1]+ans[n-1][m-2])%1000000007