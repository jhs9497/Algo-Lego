import copy

def tree_check(n, temp_wires):
    connect = [[] for _ in range(n + 1)]
    for i in range(len(temp_wires)):
        start = temp_wires[i][0]
        end = temp_wires[i][1]
        connect[start].append(end)
        connect[end].append(start)

    count_list = []
    for i in range(1, n + 1):
        visit = [False] * (n + 1)
        if connect[i] and visit[i] == False:
            visit[i] = True
            stack = []
            stack.append(i)
            while stack:
                now_point = stack.pop()
                for next_point in connect[now_point]:
                    if visit[next_point] == False:
                        visit[next_point] = True
                        stack.append(next_point)
            count_list.append(visit.count(True))
            count_list.append(visit.count(False) - 1)

    print(count_list)
    count_list = list(set(count_list))

    if len(count_list) == 1:
        return 0
    else:
        return max(count_list) - min(count_list)


def solution(n, wires):
    answer = 1e9
    for i in range(len(wires)):
        temp_wires = copy.deepcopy(wires)
        temp_wires.pop(i)
        temp_answer = tree_check(n, temp_wires)
        if temp_answer < answer:
            answer = temp_answer

    return answer