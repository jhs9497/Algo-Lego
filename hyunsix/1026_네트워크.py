def solution(n, computers):
    visited = [False] * n
    def check(start, network):
        visited[start] = True
        Q = []
        Q.append(start)
        while Q:
            now = Q.pop()
            for i in range(len(computers[now])):
                if computers[now][i] == 1 and visited[i] == False:
                    Q.append(i)
                    visited[i] = True
                    network.append(i)

        return network

    networks = []
    for i in range(len(computers)):
        if visited[i] == False:
            new_network = check(i, [i])
            networks.append(new_network)

    answer = len(networks)
    return answer