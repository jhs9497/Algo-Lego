import heapq

def solution(n, costs):
    answer = 0
    dis = [[] for _ in range(n)]
    
    for cost in costs:
        s, e, cnt = map(int, cost)
        dis[s].append([e, cnt])
        dis[e].append([s, cnt])
    
    def find(start):
        D = [[-1, 0x9999999] for _ in range(n)]

        D[start][0] = start
        D[start][1] = 0
        
        q = []
        heapq.heappush(q, (0, start))
        
        while q:
            now, cnt = heapq.heappop(q)
            if D[now][1] < cnt:
                continue
            for i in dis[now]:
                cost = i[1]
                
                if cost < D[i[0]][1]:
                    D[i[0]][1] = cost
                    D[i[0]][0] = now
                    heapq.heappush(q, (cost, i[0]))
        
        print(D)
        return D
    
    D = find(0)
    for d in D:
        answer += d[1]
    
    return answer

  # heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
  # heapq.heappop(heap)[1]) 