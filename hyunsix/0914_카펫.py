from collections import deque

def check(combi_list, total):
    for combi in combi_list:
        x = combi[0]
        y = combi[1]
        if x >= y:
            is_carpet = (x + 2) * (y + 2)
            if is_carpet == total:
                return [x + 2, y + 2]


def solution(brown, yellow):
    combi_list = deque()
    for y in range(1, yellow + 1):
        x = yellow // y
        is_combi = yellow % y
        if is_combi == 0:
            combi_list.append((x, y))

    total = brown + yellow
    answer = check(combi_list, total)

    return answer