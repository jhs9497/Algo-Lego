import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    # s = 0
    # scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:  # 한개만 남았다면
            answer = -1
            break
            # return answer
        else:  # 여러개라면
            # min_1 = scoville[s]
            # min_2 = scoville[s+1]
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville)
            new_scoville = min_1  + min_2*2
            # print(scoville)
            # new_scoville = scoville[0] + (scoville[1] * 2)
            heapq.heappush(scoville, new_scoville)
            # s = s+2
            answer += 1
            # print(scoville)

    # print(answer)

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville, K)