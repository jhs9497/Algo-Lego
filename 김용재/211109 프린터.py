from collections import deque


def solution(priorities, location):
    answer = 0
    check = [0] * len(priorities)
    check[location] = 1

    check = deque(check)
    priorities = deque(priorities)

    while 1 in check:
        max_V = max(priorities)
        a = priorities[0]
        if a >= max_V:  # 뽑힌게 제일 높으면
            priorities.popleft()
            check.popleft()
            answer += 1

        else:  # 우선순위 더 높은게 있다면
            priorities.rotate(-1)
            check.rotate(-1)
        print(answer, check, priorities)

    return answer


priorities = [2, 1, 3, 2]
location = 2
solution(priorities, location)