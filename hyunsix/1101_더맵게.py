import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        else:
            answer += 1
            pop_first = heapq.heappop(scoville)
            pop_second = heapq.heappop(scoville)
            new_scovile = pop_first + (2 * pop_second)
            heapq.heappush(scoville, new_scovile)

    if scoville[0] < K:
        answer = -1

    return answer