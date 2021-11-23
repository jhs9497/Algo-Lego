def solution(tickets):
    answer = []
    stack = []
    visited = [0] * len(tickets)
    begin = 'ICN'

    # end = tickets[0][1]
    stack.append(begin)
    answer.append(begin)

    answer = graph(tickets, stack, visited, answer)
    return answer


def graph(tickets, stack, visited, answer):
    while stack:
        begin = stack.pop(0)
        begin_candidate = []
        for i in range(len(tickets)):
            if visited[i] == 0:
                if begin == tickets[i][0]:
                    begin_candidate.append([tickets[i][1], i])
            else:
                continue
        if len(begin_candidate) == 1:
            idx = begin_candidate[0][1]
            visited[idx] = 1
            stack.append(tickets[idx][1])
            answer.append(tickets[idx][1])

        elif len(begin_candidate) > 1:
            begin_candidate.sort()
            idx = begin_candidate[0][1]
            visited[idx] = 1
            stack.append(tickets[idx][1])
            answer.append(tickets[idx][1])

        else:
            continue
        print(stack, 'stack')
        print(answer)
    return answer

tickets = [["ICN", "BBB"], ["ICN", "CCC"], ["BBB", "CCC"], ["CCC", "BBB"], ["CCC", "ICN"]]
solution(tickets)