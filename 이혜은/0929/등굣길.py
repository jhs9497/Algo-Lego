def solution(m, n, puddles):
    
    ans = [[0]*(m) for _ in range(n)]
    ans[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                continue
            if i == 0:
                ans[i][j] = ans[i][j-1]
                continue
            if j == 0:
                ans[i][j] = ans[i-1][j]
                continue
            ans[i][j] = ans[i-1][j] + ans[i][j-1]
            
    return ans[n-1][m-1]%1000000007