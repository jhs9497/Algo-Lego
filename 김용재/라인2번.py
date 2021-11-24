from collections import deque
def bfs(graph, start,end,visited,cnt):
    queue = deque([start])
    print(queue)
    visited[start] = True
    while queue:
        cnt +=1
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

                if i == end+1:
                    print()
                    print('end')
                    break
    print(cnt,'cnt')
graph = [
    [],
    [2, 3],
    [1, 3],
    [1, 2, 4, 5],
    [3, 5],
    [3, 4, 6, 7],
    [5, 7],
    [5, 6, 8],
    [7, 9, 10],
    [8, 10],
    [8, 9, 11, 12],
    [10, 12],
    [10, 11]
]
music = [1, 10, 9, 4, 5, 12]
cnt = 0
for m in range(len(music) - 1):
    start = music[m]
    end = music[m + 1]
    visited = [False] * 13
    bfs(graph,start,end,visited, cnt)

