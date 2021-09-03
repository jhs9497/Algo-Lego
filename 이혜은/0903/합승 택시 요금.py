# 2021 KAKAO BLIND RECRUITMENT
import heapq

def solution(n, s, a, b, fares):
    
    answer = 0
    dis_lst = [[-1]*(n+1) for _ in range(n+1)]
    
    for fare in fares:
        location1, location2, long = map(int, fare)
        dis_lst[location1][location2] = long
        dis_lst[location2][location1] = long
    
    def dijkstra(s):
    
        D = [0x99999999]*(n+1)
        D[s] = 0
        heap = []
        heapq.heappush(heap, (0, s))
        
        while heap:
            value, point = heapq.heappop(heap)
            if D[point] < value:
                continue
            
            for i in range(n+1):
                if dis_lst[i][point] == -1:
                    continue
                now_val, destination = dis_lst[i][point]+value, i
                if now_val < D[destination]:
                    D[destination] = now_val
                    heapq.heappush(heap, (now_val, destination))
        return D
                         
    D = [0x99999]*(n+1)
    for i in range(1, n+1):
        D[i] = dijkstra(i)

    for i in range(1, n+1):
        if answer == 0 or answer > D[i][a] + D[i][b] + D[i][s]:
            answer = D[i][a] + D[i][b] + D[i][s]

    return answer   

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
# 82
solution(8, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
# 14
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])
# 18