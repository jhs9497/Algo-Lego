# n 노드 개수, s 출발 노드번호, a 노드 위치, b 노드 위치
# fares [노드번호, 노드번호, 시간]

from math import inf #무한수
import heapq # 최소 힙

def dij(n, graph, s):
    #출발 <dist> 위치
    dist = [inf for _ in range(n)]
    #왔던길 0
    dist[s] = 0
    
    q = []
    #dist, node 큐 넣기
    heapq.heappush(q, [dist[s],s])
    while q:
        cur_dist, cur_dest = heapq.heappop(q)
        # 전 값보다 현재 값이 적으면 실행
        if dist[cur_dest] > cur_dist:
            for i in range(n):
                #새로운 거리 구하기
                new_dist = cur_dist + graph[cur_dest][i]
                if new_dist < dist[i]:
                    #새로운 거리가 이전 거리보다 작으면 실행
                    dist[i] = new_dist
                    #다음 노드를 위해 큐에 삽입
                    heapq.heappush(q, [new_dist,i])
                    
    return dist
    
    
def solution(n, s, a, b, fares):
    s = s-1
    a = a-1
    b = b-1
    #print(n,s,a,b,fares)
    graph = [[inf] * n for _ in range(n)]
    for i in fares:
        z, x, y = i
        graph[z-1][x-1] = graph[x-1][z-1] = y
        
        resultg = []
        for i in range(n):
            resultg.append(dij(n, graph, i))
            
        value = inf
        for i in range(n):
            value = min(value, resultg[s][i] + resultg[i][a] + resultg[i][b])

    return value
