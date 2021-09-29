def solution(m, n, puddles):
    zido = [[0]*(m) for _ in range(n)]
    zido[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1,i+1] in puddles:
                zido[i][j] = 0
            else:
                zido[i][j] += (zido[i-1][j] + zido[i][j-1])
    count = zido[-1][-1] % 1000000007

    return count