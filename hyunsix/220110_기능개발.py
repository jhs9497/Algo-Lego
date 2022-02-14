def solution(progresses, speeds):
    answer = []
    while progresses:

        for j in range(len(progresses)):
            progresses[j] += speeds[j]

        pop_list = []
        if progresses[0] >= 100:
            pop_list.append(0)
            for i in range(1, len(progresses)):
                if progresses[i] >= 100 and progresses[i - 1] >= 100:
                    pop_list.append(i)
                elif progresses[i] < 100:
                    break

        L = len(pop_list)
        if L > 0:
            answer.append(L)
            for k in range(L - 1, -1, -1):
                progresses.pop(k)
                speeds.pop(k)

    return answer