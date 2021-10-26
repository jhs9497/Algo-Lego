def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def bfs(k):
        s = []
        visited[k] = True
        s.append(k)
        while s:
            k = s.pop()
            for l in range(len(computers[k])):
                # 만일 자신이 서있는 위치라면
                if k == l:
                    continue
                # 만일 연결이 되어있지 않다면
                if computers[k][l] == 0:
                    continue
                # 만일 이미 방문했다면
                if visited[l] == True:
                    continue
                s.append(l)
                visited[l] = True
            
    for i in range(n):
        if visited[i]:
            continue
        bfs(i)
        answer += 1
    
    return answer