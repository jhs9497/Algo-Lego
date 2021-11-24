from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    answer = [0] * len(prices)
    i = 0
    while prices:
        a = prices.popleft()
        for p in prices:
            if p < a: # 작으면
                answer[i] += 1
                break
            else: # 크면
                answer[i] += 1
        i += 1
    return answer