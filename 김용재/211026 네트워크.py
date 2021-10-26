def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(i):
        stack = []
        stack.append(i)
        visited[i] = True

        while stack:
            i = stack.pop(-1)
            for idx in range(len(computers[i])):
                if computers[i][idx] == 1 and visited[idx] == False:
                    visited[idx] = True
                    stack.append(idx)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer



